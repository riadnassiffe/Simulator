/*
    Copyright (c) <year>, <copyright holder>
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:
        * Redistributions of source code must retain the above copyright
        notice, this list of conditions and the following disclaimer.
        * Redistributions in binary form must reproduce the above copyright
        notice, this list of conditions and the following disclaimer in the
        documentation and/or other materials provided with the distribution.
        * Neither the name of the <organization> nor the
        names of its contributors may be used to endorse or promote products
        derived from this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY <copyright holder> ''AS IS'' AND ANY
    EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL <copyright holder> BE LIABLE FOR ANY
    DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
    ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

*/

#include "task.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void Task::loadTask(int numeroTarefa, int numeroDeModos, int numeroDeFrequncias,char *path)
{
	string line;
	string line2;
	string line3;
	string line4;

	string b;
	string a;
	b = path;
	a = b + "utilizacao.txt";
	ifstream myfile(a.c_str());
	a=b + "beneficio.txt";
	ifstream myfile2(a.c_str());
	a = b + "P.txt";
	ifstream myfile3(a.c_str());

	int i = 0;
	int j = 0;

	if (myfile.is_open()) {
		for (int k=0;k<(numeroTarefa)*numeroDeFrequncias*numeroDeModos;k++){
			getline(myfile, line);
			getline(myfile2, line2);
			getline(myfile3, line3);
		}
		while (!myfile.eof() and i<numeroDeModos) {
			getline(myfile, line);
			getline(myfile2, line2);
			getline(myfile3, line3);

			recursoUtilizado[i][j] = atof(line.c_str());
			beneficio[i][j] = atof(line2.c_str());
			energia[i][j] = atof(line3.c_str());
			if (j == numeroDeFrequncias-1) {
				i++;
				j = 0;
			}else{
				j++;
			}
		}
		myfile.close();
		myfile2.close();
		myfile3.close();
	} else
		cout << "Unable to open file";

}

Task::Task()
{

}


Task::Task(int numeroDeModos,int numeroDeFrequencias)
{

}

float Task::getEnergia(int mod, int freq)
{
  return energia[mod][freq];
}

float Task::getBeneficio(int mod,int freq)
{
   return beneficio[mod][freq];
}
float Task::getRecursoUtilizado(int mod, int freq)
{
   return recursoUtilizado[mod][freq];
}

Task::~Task()
{

}
