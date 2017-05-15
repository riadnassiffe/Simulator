/*
 * dataHandler.c
 *
 *  Created on: May 21, 2012
 *      Author: riad
 */

#include"dataHandler.h"

/*int main() {
	char *file = malloc(20 * sizeof(char));
	file = "data.xml";
	readFile(file);
	return 0;
}*/

struct problemData *readFile(const char *fileName) {
	struct problemData *p;
	xmlDocPtr doc;
	xmlNodePtr nodeLevel0;
	xmlNodePtr nodeLevel1;
	xmlNodePtr nodeLevel2;
	xmlChar *name;


	doc = xmlParseFile(fileName);
	nodeLevel0 = doc->children;
	//alocando dados dentro da estrutura para guardar as informações das tarefas
	name=xmlGetProp(nodeLevel0,(const xmlChar *) "tasks");
	int numTasks=atoi(name);

	p = malloc(sizeof(struct problemData));
	p->numTasks=numTasks;


	int i;
	for (nodeLevel1 = nodeLevel0->children; nodeLevel1 != NULL; nodeLevel1 = nodeLevel1->next) {
		if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "B1"))) {
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->B1=xmlXPathCastStringToNumber(name);
				}
			}
		} else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "B2"))) {
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->B2=xmlXPathCastStringToNumber(name);
				}
			}
		} else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "CdMax"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->Cd[i]=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
		}else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "CI"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->Ci[i]=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
		}else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "Fmin"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->Fmin[i]=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
		} else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "T"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->T[i]=xmlXPathCastStringToNumber(name);

					i++;
				}
			}
		}else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "Pi"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->Pi[i]=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
		}else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "W"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->W[i]=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
	    }else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "a"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->a=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
	    }else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "b"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->b=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
	    }else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "H"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->H=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
	    }else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "Hmax"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->Hmax=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
	    }else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "Hamb"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->Hamb=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
	    }else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "C0"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->C0=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
	    }else if (!(xmlStrcmp(nodeLevel1->name, (const xmlChar *) "W2"))) {
			i=0;
			for (nodeLevel2 = nodeLevel1->children; nodeLevel2 != NULL;
					nodeLevel2 = nodeLevel2->next) {
				if (!(xmlStrcmp(nodeLevel2->name, (const xmlChar *) "variable"))) {
					name = xmlNodeGetContent(nodeLevel2);
					p->W2[i]=xmlXPathCastStringToNumber(name);
					i++;
				}
			}
	    }										

	}
	return p;

}
