#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""More fun with lists."""

import data


BALLETS = data.BALLETS
del BALLETS[11]
BALLETS[1] = 'Swan Lake'
BALLETS.append('Herman Scherman')
BALLETS.extend(['Don Quixote', 'Sylvia'])