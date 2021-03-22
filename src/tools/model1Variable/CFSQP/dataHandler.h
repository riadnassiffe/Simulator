/*
 * dataHandler.h
 *
 *  Created on: May 21, 2012
 *      Author: riad
 */

#ifndef DATAHANDLER_H_

#define DATAHANDLER_H_
#include"problem.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#include <libxml/xmlreader.h>
#include <libxml/parser.h>
#include <libxml/tree.h>
#include <libxml/encoding.h>
#include <libxml/xpath.h>

#ifdef LIBXML_READER_ENABLED
#endif


struct problemData *readFile(const char *fileName);

#endif /* DATAHANDLER_H_ */
