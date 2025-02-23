#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;

    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    for (int i =0; i< voter_count;i++){
        for (int j = 0; j < candidate_count; j++){
        printf("%d , ", preferences[i][j]);
        }
        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();

        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();

        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if(candidates[i].eliminated == false){
                printf("%s\n", candidates[i].name);
            }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }


    }

        //Find the candidate that got eliminated

        return 0;
        //Make their second AND third votes become their first vote.
    }



// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{

    for (int i = 0; i< candidate_count; i++){
   if(strcmp(name, candidates[i].name) == 0){
        preferences[voter][rank] = i;
        return true;
   }
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{

    int x, y, z;

    for (int i =0; i < voter_count;i++){

        x = preferences[i][0];
        y = preferences[i][1];
        z = preferences[i][2];

        if(candidates[x].eliminated == true && candidates[y].eliminated == true){
            candidates[z].votes +=1;
        } else if(candidates[x].eliminated == true){
            candidates[y].votes +=1;
        } else {

     candidates[x].votes += 1;
    }
    }

        for (int i=0; i< candidate_count;i++){
        printf("Candidate name: %s , Current votes: %d\n", candidates[i].name, candidates[i].votes);
        }

    return;

    //This function should give you the initial rankings of the votes
}

// Print the winner of the election, if there is one
bool print_winner(void)
{

    int winner = candidates[0].votes;
    string winnercandidate;

    //First find the highest data set value in the struct

    for (int i = 0; i < candidate_count-1; i++){

        if (winner < candidates[i+1].votes){
            winner = candidates[i+1].votes;
        }
    }

    printf("The highest number of votes is: %d\n", winner);

       if(winner != 0){
    for (int i=0; i< candidate_count;i ++){

        if(winner == candidates[i].votes){
            winnercandidate =  candidates[i].name;
        }
    }
    }

    float isfifty = (double) winner / voter_count;
    printf("--------- %f -------\n",  isfifty);

    if(isfifty > 0.5){

        printf("The winner is: %s\n", winnercandidate);
        return true;
    } else{
        printf("Round one no suitable candidate found\n");
        return false;
    }



}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{

    int smallest =0;

    for (int j =0; j <candidate_count; j++){
        if(candidates[j].eliminated != true){
            smallest = candidates[j].votes;
            break;
        }
    }


    for (int j =0; j <candidate_count; j++){
        if(candidates[j].eliminated != true){
            if(smallest > candidates[j].votes){
            smallest = candidates[j].votes;
            }
        }
    }

    printf("MINIMUM VOTES: %d\n", smallest);
    return smallest;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    // TODO
    int checktie = 0;
    int eliminated_count = 0;

    for(int i=0; i < candidate_count; i++){
        if(candidates[i].eliminated == true){
            eliminated_count += 1;
        }
    }

    for (int i=0; i< candidate_count; i++){

        if(candidates[i].eliminated == false){
            if(candidates[i].votes == min){
            checktie += 1;
        }
        }
    }


    if(checktie == candidate_count - eliminated_count){
        printf("There is a tie\n");
        return true;
    } else {
        printf("There is no tie\n");
        return false;
}
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    for (int i=0; i< candidate_count; i++){
        if(candidates[i].votes == min){
            candidates[i].eliminated = true;
            printf("Candidate eliminated: %s\n", candidates[i].name);
        }
    }
    return;
}