#include <vector>
#include <tuple>
#include <stdlib.h>

#include "env.h"

using namespace std;
using namespace dun;

// implementation of class functions
void Dungeon::set_player_location() {
  // randomly initialize the player location
  srand (time(0));
  int x = rand() % grid_size;
  int y = rand() % grid_size;
  agent_position = make_tuple(x,y);
}

// return player location
tuple<int, int> Dungeon::get_player_location() { return agent_position; }

// randomly set the enemies location
void Dungeon::set_enemy_positions(tuple<int, int> ag_pos){
  srand (time(0));

  // generate num enemies position
  for (int i = 0; i < num_enemies; i++){
    int x = rand() % grid_size;
    int y = rand() % grid_size;
    tuple<int, int> position = make_tuple(x,y);

    // we don't want to spawn an enemy at the agents location
    while (position == ag_pos){
      srand (time(0));
      int x = rand() % grid_size;
      int y = rand() % grid_size;
      position = make_tuple(x,y);
    }

    // update vector
    enemy_position.push_back(position);
  }
}

// return location of all enemies
vector<tuple<int, int>> Dungeon::get_enemy_positions(){ return enemy_position; }

//TODO:
// 1) state representation functions
// 2) environment functions

// constructor
Dungeon::Dungeon(int gs, int nm) {
  grid_size = gs;
  num_enemies = nm;
  set_player_location();
  set_enemy_positions(get_player_location());
}
