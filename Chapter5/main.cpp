#include "env.h"
#include <iostream>
#include <stdlib.h>
#include <tuple>

using namespace dun;
using namespace std;

int main(){
  Dungeon dungeon = Dungeon(100, 5);
  dungeon.set_player_location(); 
  dungeon.set_enemy_positions(dungeon.get_player_location());
  cout << "Enemy location\n";
  for (tuple<int,int> position : dungeon.get_enemy_positions()){
    cout << get<0>(position) << " " << get<1>(position) << "\n";
  }
  cout << "Player location \n";
  cout << get<0>(dungeon.agent_position) << " " << get<1>(dungeon.agent_position) << "\n";
}

