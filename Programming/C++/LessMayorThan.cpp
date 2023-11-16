#include <iostream>
using namespaces std;

int num1 = 0, num2 = 0;
int LessMayorThan(int num1, int num2){
  if(num1 > num2){return num1;} 
  else {return num2;}
}

int main(){
  cout<<"Introduzca el valor del primer número: "<<endl;
  cin>>num1;
  cout<<"Introduzca el valor del segundo número: "<<endl;
  cin>>num2;
  cout<<"Entre "<<num1<<" y "<<num2<<", el mayor es "<<LessMayorThan(num1, num2)<<endl;
  return 0;
}