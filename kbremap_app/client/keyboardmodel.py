# This file is part of the kbremap project.
# Copyright (C) 2014 Nicolas Malarmey
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
# contact: elmamyra@gmail.com

"""
Data of keyboard models.
"""


EMPTY, SPACE, RETURN = range(-4, -1)

keyboardModels = {
'generic_101': (
            (22.5, 6),
            (   #row 0
                (9, (1, 2.0/3)),
                (-1, (1, 1), SPACE),
                (67, (1, 2.0/3)),
                (68, (1, 2.0/3)),
                (69, (1, 2.0/3)),
                (70, (1, 2.0/3)),
                (-1, (0.5, 1), SPACE),
                (71, (1, 2.0/3)),
                (72, (1, 2.0/3)),
                (73, (1, 2.0/3)),
                (74, (1, 2.0/3)),
                (-1, (0.5, 1), SPACE),
                (75, (1, 2.0/3)),
                (76, (1, 2.0/3)),
                (95, (1, 2.0/3)),
                (96, (1, 2.0/3)),
                (-1, (0.25, 1), SPACE),
                (107, (1, 2.0/3)),
                (78, (1, 2.0/3)),
                (127, (1, 2.0/3)),
               
            ),
            (   #row 1
                (49, (1, 1)),
                (10, (1, 1)),
                (11, (1, 1)),
                (12, (1, 1)),
                (13, (1, 1)),
                (14, (1, 1)),
                (15, (1, 1)),
                (16, (1, 1)),
                (17, (1, 1)),
                (18, (1, 1)),
                (19, (1, 1)),
                (20, (1, 1)),
                (21, (1, 1)),
                (22, (2, 1)),
                (-1, (0.25, 1), SPACE),
                (118, (1, 1)),
                (110, (1, 1)),
                (112, (1, 1)),
                (-1, (0.25, 1), SPACE),
                (77, (1, 1)),
                (106, (1, 1)),
                (63, (1, 1)),
                (82, (1, 1)),
            ),
            (   #row 2
                (23, (1.5, 1)),
                (24, (1, 1)),
                (25, (1, 1)),
                (26, (1, 1)),
                (27, (1, 1)),
                (28, (1, 1)),
                (29, (1, 1)),
                (30, (1, 1)),
                (31, (1, 1)),
                (32, (1, 1)),
                (33, (1, 1)),
                (34, (1, 1)),
                (35, (1, 1)),
                (51, (1.5, 1)),
                (-1, (0.25, 1), SPACE),
                (119, (1, 1)),
                (115, (1, 1)),
                (117, (1, 1)),
                (-1, (0.25, 1), SPACE),
                (79, (1, 1)),
                (80, (1, 1)),
                (81, (1, 1)),
                (86, (1, 2)),
            ),
            (   #row 3
                (66, (7.0/4, 1)),
                (38, (1, 1)),
                (39, (1, 1)),
                (40, (1, 1)),
                (41, (1, 1)),
                (42, (1, 1)),
                (43, (1, 1)),
                (44, (1, 1)),
                (45, (1, 1)),
                (46, (1, 1)),
                (47, (1, 1)),
                (48, (1, 1)),
                (36, (9.0/4, 1)),
                (-1, (3.5, 1), SPACE),
                (83, (1, 1)),
                (84, (1, 1)),
                (85, (1, 1)),
                (-1, (1, 1), SPACE),
            ),
            (   #row 4
                (50, (9.0/4, 1)),
                (52, (1, 1)),
                (53, (1, 1)),
                (54, (1, 1)),
                (55, (1, 1)),
                (56, (1, 1)),
                (57, (1, 1)),
                (58, (1, 1)),
                (59, (1, 1)),
                (60, (1, 1)),
                (61, (1, 1)),
                (62, (11.0/4, 1)),
                (-1, (1.25, 1), SPACE),
                (111, (1, 1)),
                (-1, (1.25, 1), SPACE),
                (87, (1, 1)),
                (88, (1, 1)),
                (89, (1, 1)),
                (104, (1, 2)),
                
            ),
            (   #row 5
                (37, (1.5, 1)),
                (-1, (1, 1), SPACE),
                (64, (1.5, 1)),
                (65, (7, 1)),
                (108, (1.5, 1)),
                (-1, (1, 1), SPACE),
                (105, (1.5, 1)),
                (-1, (0.25, 1), SPACE),
                (113, (1, 1)),
                (116, (1, 1)),
                (114, (1, 1)),
                (-1, (0.25, 1), SPACE),
                (90, (2, 1)),
                (91, (1, 1)),
                (-1, (1, 1), SPACE),
            )
        ),
                  
'generic_102': (
            (22.5, 6),
            (   #row 0
                (9, (1, 2.0/3)),
                (-1, (1, 1), SPACE),
                (67, (1, 2.0/3)),
                (68, (1, 2.0/3)),
                (69, (1, 2.0/3)),
                (70, (1, 2.0/3)),
                (-1, (0.5, 1), SPACE),
                (71, (1, 2.0/3)),
                (72, (1, 2.0/3)),
                (73, (1, 2.0/3)),
                (74, (1, 2.0/3)),
                (-1, (0.5, 1), SPACE),
                (75, (1, 2.0/3)),
                (76, (1, 2.0/3)),
                (95, (1, 2.0/3)),
                (96, (1, 2.0/3)),
                (-1, (0.25, 1), SPACE),
                (107, (1, 2.0/3)),
                (78, (1, 2.0/3)),
                (127, (1, 2.0/3)),
               
            ),
            (   #row 1
                (49, (1, 1)),
                (10, (1, 1)),
                (11, (1, 1)),
                (12, (1, 1)),
                (13, (1, 1)),
                (14, (1, 1)),
                (15, (1, 1)),
                (16, (1, 1)),
                (17, (1, 1)),
                (18, (1, 1)),
                (19, (1, 1)),
                (20, (1, 1)),
                (21, (1, 1)),
                (22, (2, 1)),
                (-1, (0.25, 1), SPACE),
                (118, (1, 1)),
                (110, (1, 1)),
                (112, (1, 1)),
                (-1, (0.25, 1), SPACE),
                (77, (1, 1)),
                (106, (1, 1)),
                (63, (1, 1)),
                (82, (1, 1)),
            ),
            (   #row 2
                (23, (1.5, 1)),
                (24, (1, 1)),
                (25, (1, 1)),
                (26, (1, 1)),
                (27, (1, 1)),
                (28, (1, 1)),
                (29, (1, 1)),
                (30, (1, 1)),
                (31, (1, 1)),
                (32, (1, 1)),
                (33, (1, 1)),
                (34, (1, 1)),
                (35, (1, 1)),
                (36, (1.5, 2), RETURN),
                (-1, (0.25, 1), SPACE),
                (119, (1, 1)),
                (115, (1, 1)),
                (117, (1, 1)),
                (-1, (0.25, 1), SPACE),
                (79, (1, 1)),
                (80, (1, 1)),
                (81, (1, 1)),
                (86, (1, 2)),
            ),
            (   #row 3
                (66, (7.0/4, 1)),
                (38, (1, 1)),
                (39, (1, 1)),
                (40, (1, 1)),
                (41, (1, 1)),
                (42, (1, 1)),
                (43, (1, 1)),
                (44, (1, 1)),
                (45, (1, 1)),
                (46, (1, 1)),
                (47, (1, 1)),
                (48, (1, 1)),
                (51, (1, 1)),
                (-1, (5.0/4, 1), SPACE),
                (-1, (3.5, 1), SPACE),
                (83, (1, 1)),
                (84, (1, 1)),
                (85, (1, 1)),
                (-1, (1, 1), SPACE),
                
            ),
            (   #row 4
                (50, (4.0/3, 1)),
                (94, (1, 1)),
                (52, (1, 1)),
                (53, (1, 1)),
                (54, (1, 1)),
                (55, (1, 1)),
                (56, (1, 1)),
                (57, (1, 1)),
                (58, (1, 1)),
                (59, (1, 1)),
                (60, (1, 1)),
                (61, (1, 1)),
                (62, (8.0/3, 1)),
                (-1, (1.25, 1), SPACE),
                (111, (1, 1)),
                (-1, (1.25, 1), SPACE),
                (87, (1, 1)),
                (88, (1, 1)),
                (89, (1, 1)),
                (104, (1, 2)),
            ),
            (   #row 5
                (37, (1.5, 1)),
                (-1, (1, 1), SPACE),
                (64, (1.5, 1)),
                (65, (7, 1)),
                (108, (1.5, 1)),
                (-1, (1, 1), SPACE),
                (105, (1.5, 1)),
                (-1, (0.25, 1), SPACE),
                (113, (1, 1)),
                (116, (1, 1)),
                (114, (1, 1)),
                (-1, (0.25, 1), SPACE),
                (90, (2, 1)),
                (91, (1, 1)),
                (-1, (1, 1), SPACE),
            )
        ),                                    

'generic_104': (
            (22.5, 6),
            (   #row 0
                (9, (1, 2.0/3)),
                (-1, (1, 1), SPACE),
                (67, (1, 2.0/3)),
                (68, (1, 2.0/3)),
                (69, (1, 2.0/3)),
                (70, (1, 2.0/3)),
                (-1, (0.5, 1), SPACE),
                (71, (1, 2.0/3)),
                (72, (1, 2.0/3)),
                (73, (1, 2.0/3)),
                (74, (1, 2.0/3)),
                (-1, (0.5, 1), SPACE),
                (75, (1, 2.0/3)),
                (76, (1, 2.0/3)),
                (95, (1, 2.0/3)),
                (96, (1, 2.0/3)),
                (-1, (0.25, 1), SPACE),
                (107, (1, 2.0/3)),
                (78, (1, 2.0/3)),
                (127, (1, 2.0/3)),
               
            ),
            (   #row 1
                (49, (1, 1)),
                (10, (1, 1)),
                (11, (1, 1)),
                (12, (1, 1)),
                (13, (1, 1)),
                (14, (1, 1)),
                (15, (1, 1)),
                (16, (1, 1)),
                (17, (1, 1)),
                (18, (1, 1)),
                (19, (1, 1)),
                (20, (1, 1)),
                (21, (1, 1)),
                (22, (2, 1)),
                (-1, (0.25, 1), SPACE),
                (118, (1, 1)),
                (110, (1, 1)),
                (112, (1, 1)),
                (-1, (0.25, 1), SPACE),
                (77, (1, 1)),
                (106, (1, 1)),
                (63, (1, 1)),
                (82, (1, 1)),
            ),
            (   #row 2
                (23, (1.5, 1)),
                (24, (1, 1)),
                (25, (1, 1)),
                (26, (1, 1)),
                (27, (1, 1)),
                (28, (1, 1)),
                (29, (1, 1)),
                (30, (1, 1)),
                (31, (1, 1)),
                (32, (1, 1)),
                (33, (1, 1)),
                (34, (1, 1)),
                (35, (1, 1)),
                (51, (1.5, 1)),
                (-1, (0.25, 1), SPACE),
                (119, (1, 1)),
                (115, (1, 1)),
                (117, (1, 1)),
                (-1, (0.25, 1), SPACE),
                (79, (1, 1)),
                (80, (1, 1)),
                (81, (1, 1)),
                (86, (1, 2)),
            ),
            (   #row 3
                (66, (7.0/4, 1)),
                (38, (1, 1)),
                (39, (1, 1)),
                (40, (1, 1)),
                (41, (1, 1)),
                (42, (1, 1)),
                (43, (1, 1)),
                (44, (1, 1)),
                (45, (1, 1)),
                (46, (1, 1)),
                (47, (1, 1)),
                (48, (1, 1)),
                (36, (9.0/4, 1)),
                (-1, (3.5, 1), SPACE),
                (83, (1, 1)),
                (84, (1, 1)),
                (85, (1, 1)),
                (-1, (1, 1), SPACE),
            ),
            (   #row 4
                (50, (9.0/4, 1)),
                (52, (1, 1)),
                (53, (1, 1)),
                (54, (1, 1)),
                (55, (1, 1)),
                (56, (1, 1)),
                (57, (1, 1)),
                (58, (1, 1)),
                (59, (1, 1)),
                (60, (1, 1)),
                (61, (1, 1)),
                (62, (11.0/4, 1)),
                (-1, (1.25, 1), SPACE),
                (111, (1, 1)),
                (-1, (1.25, 1), SPACE),
                (87, (1, 1)),
                (88, (1, 1)),
                (89, (1, 1)),
                (104, (1, 2)),
            ),
            (   #row 5
                (37, (1.5, 1)),
                (133, (5.0/4, 1)),
                (64, (5.0/4, 1)),
                (65, (6, 1)),
                (108, (5.0/4, 1)),
                (134, (5.0/4, 1)),
                (135, (5.0/4, 1)),
                (105, (5.0/4, 1)),
                (-1, (0.25, 1), SPACE),
                (113, (1, 1)),
                (116, (1, 1)),
                (114, (1, 1)),
                (-1, (0.25, 1), SPACE),
                (90, (2, 1)),
                (91, (1, 1)),
                (-1, (1, 1), SPACE),
            )
        ),

'generic_105': (
            (22.5, 6),
            (   #row 0
                (9, (1, 2.0/3)),
                (-1, (1, 1), SPACE),
                (67, (1, 2.0/3)),
                (68, (1, 2.0/3)),
                (69, (1, 2.0/3)),
                (70, (1, 2.0/3)),
                (-1, (0.5, 1), SPACE),
                (71, (1, 2.0/3)),
                (72, (1, 2.0/3)),
                (73, (1, 2.0/3)),
                (74, (1, 2.0/3)),
                (-1, (0.5, 1), SPACE),
                (75, (1, 2.0/3)),
                (76, (1, 2.0/3)),
                (95, (1, 2.0/3)),
                (96, (1, 2.0/3)),
                (-1, (0.25, 1), SPACE),
                (107, (1, 2.0/3)),
                (78, (1, 2.0/3)),
                (127, (1, 2.0/3)),
               
            ),
            (   #row 1
                (49, (1, 1)),
                (10, (1, 1)),
                (11, (1, 1)),
                (12, (1, 1)),
                (13, (1, 1)),
                (14, (1, 1)),
                (15, (1, 1)),
                (16, (1, 1)),
                (17, (1, 1)),
                (18, (1, 1)),
                (19, (1, 1)),
                (20, (1, 1)),
                (21, (1, 1)),
                (22, (2, 1)),
                (-1, (0.25, 1), SPACE),
                (118, (1, 1)),
                (110, (1, 1)),
                (112, (1, 1)),
                (-1, (0.25, 1), SPACE),
                (77, (1, 1)),
                (106, (1, 1)),
                (63, (1, 1)),
                (82, (1, 1)),
            ),
            (   #row 2
                (23, (1.5, 1)),
                (24, (1, 1)),
                (25, (1, 1)),
                (26, (1, 1)),
                (27, (1, 1)),
                (28, (1, 1)),
                (29, (1, 1)),
                (30, (1, 1)),
                (31, (1, 1)),
                (32, (1, 1)),
                (33, (1, 1)),
                (34, (1, 1)),
                (35, (1, 1)),
                (36, (1.5, 2), RETURN),
                (-1, (0.25, 1), SPACE),
                (119, (1, 1)),
                (115, (1, 1)),
                (117, (1, 1)),
                (-1, (0.25, 1), SPACE),
                (79, (1, 1)),
                (80, (1, 1)),
                (81, (1, 1)),
                (86, (1, 2)),
                
            ),
            (   #row 3
                (66, (7.0/4, 1)),
                (38, (1, 1)),
                (39, (1, 1)),
                (40, (1, 1)),
                (41, (1, 1)),
                (42, (1, 1)),
                (43, (1, 1)),
                (44, (1, 1)),
                (45, (1, 1)),
                (46, (1, 1)),
                (47, (1, 1)),
                (48, (1, 1)),
                (51, (1, 1)),
                (-1, (5.0/4, 1), SPACE),
                (-1, (3.5, 1), SPACE),
                (83, (1, 1)),
                (84, (1, 1)),
                (85, (1, 1)),
                (-1, (1, 1), SPACE),
            ),
            (   #row 4
                (50, (4.0/3, 1)),
                (94, (1, 1)),
                (52, (1, 1)),
                (53, (1, 1)),
                (54, (1, 1)),
                (55, (1, 1)),
                (56, (1, 1)),
                (57, (1, 1)),
                (58, (1, 1)),
                (59, (1, 1)),
                (60, (1, 1)),
                (61, (1, 1)),
                (62, (8.0/3, 1)),
                (-1, (1.25, 1), SPACE),
                (111, (1, 1)),
                (-1, (1.25, 1), SPACE),
                (87, (1, 1)),
                (88, (1, 1)),
                (89, (1, 1)),
                (104, (1, 2)),
            ),
            (   #row 5
                (37, (1.5, 1)),
                (133, (5.0/4, 1)),
                (64, (5.0/4, 1)),
                (65, (6, 1)),
                (108, (5.0/4, 1)),
                (134, (5.0/4, 1)),
                (135, (5.0/4, 1)),
                (105, (5.0/4, 1)),
                (-1, (0.25, 1), SPACE),
                (113, (1, 1)),
                (116, (1, 1)),
                (114, (1, 1)),
                (-1, (0.25, 1), SPACE),
                (90, (2, 1)),
                (91, (1, 1)),
                (-1, (1, 1), SPACE),
            )
        ),

        'typeMatrix': (
            (19.5, 7),
            (
                (9, (1, 2.0/3, 1.0/3)),
                (67, (1, 2.0/3, 1.0/3)),
                (68, (1, 2.0/3, 1.0/3)),
                (69, (1, 2.0/3, 1.0/3)),
                (70, (1, 2.0/3, 1.0/3)),
                (71, (1, 2.0/3, 1.0/3)),
                (119, (1, 1, 1.0/3)),
                (72, (1, 2.0/3, 1.0/3)),
                (73, (1, 2.0/3, 1.0/3)),
                (74, (1, 2.0/3, 1.0/3)),
                (75, (1, 2.0/3, 1.0/3)),
                (76, (1, 2.0/3, 1.0/3)),
                (95, (1, 2.0/3, 1.0/3)),
                (96, (1, 2.0/3, 1.0/3)),
                (77, (1, 2.0/3, 1.0/3)),
            ),
            
            (   #row 1
                (49, (1, 1)),
                (10, (1, 1)),
                (11, (1, 1)),
                (12, (1, 1)),
                (13, (1, 1)),
                (14, (1, 1)),
                (22, (1, 5.0/3, 1.0/3)),
                (15, (1, 1)),
                (16, (1, 1)),
                (17, (1, 1)),
                (18, (1, 1)),
                (19, (1, 1)),
                (20, (1, 1)),
                (21, (1, 1)),
                (-1, (1, 1), EMPTY),
                (-1, (0.5, 1), SPACE),
                (77, (1, 1)),
                (106, (1, 1)),
                (63, (1, 1)),
                (82, (1, 1)),                
            ),
            (   #row 2
                (23, (1, 1)),
                (24, (1, 1)),
                (25, (1, 1)),
                (26, (1, 1)),
                (27, (1, 1)),
                (28, (1, 1)),
                (-1, (1, 1), SPACE),
                (29, (1, 1)),
                (30, (1, 1)),
                (31, (1, 1)),
                (32, (1, 1)),
                (33, (1, 1)),
                (34, (1, 1)),
                (35, (1, 1)),
                (-1, (1, 1), EMPTY),
                (-1, (0.5, 1), SPACE),
                (79, (1, 1)),
                (80, (1, 1)),
                (81, (1, 1)),
                (86, (1, 2)),
            ),
            (   #row 3
                (50, (1, 2)),
                (38, (1, 1)),
                (39, (1, 1)),
                (40, (1, 1)),
                (41, (1, 1)),
                (42, (1, 1)),
                (36, (1, 2)),
                (43, (1, 1)),
                (44, (1, 1)),
                (45, (1, 1)),
                (46, (1, 1)),
                (47, (1, 1)),
                (48, (1, 1)),
                (50, (1, 2)),
                (66, (1, 1)),
                (-1, (0.5, 1), SPACE),
                (83, (1, 1)),
                (84, (1, 1)),
                (85, (1, 1)),
                (-1, (1, 1), SPACE),
                
            ),
            (   #row 4
                (-1, (1, 1), SPACE),
                (52, (1, 1)),
                (53, (1, 1)),
                (54, (1, 1)),
                (55, (1, 1)),
                (56, (1, 1)),
                (-1, (1, 1), SPACE),
                (57, (1, 1)),
                (58, (1, 1)),
                (59, (1, 1)),
                (60, (1, 1)),
                (61, (1, 1)),
                (51, (1, 1)),
                (-1, (1, 1), SPACE),
                (-1, (1, 1), EMPTY),
                (-1, (0.5, 1), SPACE),
                (87, (1, 1)),
                (88, (1, 1)),
                (89, (1, 1)),
                (104, (1, 2)),
            ),
            (   #row 5
                (37, (1, 1)),
                (-1, (1, 1), EMPTY),
                (135, (1, 1)),
                (-1, (1, 1), EMPTY),
                (65, (5, 4.0/3)),
                (-1, (1, 1), EMPTY),
                (110, (1, 1)),
                (111, (1, 1)),
                (115, (1, 1)),
                (105, (1, 2)),
                (112, (1, 1)),
                (-1, (0.5, 1), SPACE),
                (90, (2, 1)),
                (91, (1, 1)),
                (-1, (1, 1), SPACE),                
            ),
            (   #row 6
                (-1, (1, 1), EMPTY),
                (133, (1.5, 1)),
                (64, (1.5, 1)),
                (-1, (5, 1), SPACE),
                (108, (1, 1)),
                (113, (1, 1)),
                (116, (1, 1)),
                (114, (1, 1)),
                (-1, (1, 1), SPACE),
                (117, (1, 1)),
            )
        )
}