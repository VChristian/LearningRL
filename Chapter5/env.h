// env.h 
// Begin with a simple environment

#include <iostream>
#include <tuple> // for tuple
#include <vector>
using namespace std;

namespace dun
{
    class Dungeon
    {
    public:

        // state data structure for our dungeon 
        struct state
        {
          tuple<int, int> ap;
          vector<tuple<int,int>> enemy_position;
        };
        
        // environment init information
        int grid_size;
        int num_enemies;
        
        // Agent and enemy information
        tuple<int, int> agent_position;
        vector<tuple<int,int>> enemy_position;
        
        // state of environment
        state env_state;

        // constructor and setting up environment
        Dungeon(int grid_size, int num_enemies);

        // player position functions
        void set_player_location();
        tuple<int, int> get_player_location();

        // enemy position functions
        void set_enemy_positions(tuple<int, int> ag_pos);
        vector<tuple<int,int>> get_enemy_positions();

        // environment state functions
        void set_env_state(tuple<int, int> ag_pos, vector<tuple<int, int>> enemy_position);
        state get_env_state();

        // env functions
        void step(int mv);
        int reward(tuple<int, int> ag_pos, vector<tuple<int,int>> en_pos, int mv);
        state reset();
    };
}
