#include <iostream>
#include<iomanip>

int main()
{
  int num_blocks;
  int weight_limit;
  int height_of_tower(0);
  cout << "Enter the number of the blocks" << endl;
  cin >> num_blocks;
  int temp_num_blocks(num_blocks);
  cout << "enter the weight limit of the block" << ednl;
  cin >> weight_limit;
  while(temp_num_blocks / (weight_limit + 1) <= temp_num_blocks)
    {
      if(temp_num_blocks % (weight_limit + 1) == 0)
      {
        temp_num_blocks -= temp_num_blocks / (weight_limit + 1);
      }
      else
      {
        temp_num_blocks -= temp_num_blocks / (weight_limit + 1) + 1;
      }
      height_of_tower++;
    }
  cout << "The highest tower floor is " << height_of_tower << endl;
  
}
