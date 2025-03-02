#include<iostream>
#include<iomanip>

main()
{
  int num_of_station;
  int num_of_stop;
  int num_of_start;
  int list_of_stop;
  cout << "Enter the number of stations" << endl;
  cin >> num_of_station;
  cout << "Enter the number of stations you stop" << endl;
  cin >> num_of_stop;
  cout << "Enter the number of the station you start" << endl;
  cin >> num_of_start;
  do
    {
      cout << "Enter the number of the station you stop(0 to quit)" << endl;
      cin >> num_of_stop;
      
    }
  while(num_of_stop != 0);
}
