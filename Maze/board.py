import pygame

class GameBoard:
    def __init__(self):
        self.board = pygame.image.load("game_board.png")
        self.board_x = 0
        self.board_y = 0

        self.rect_1 = pygame.Rect(112,-106,8,600)

        self.rect_2 = pygame.Rect(112,528,8,500)
        
        self.rect_3 = pygame.Rect(112,528,50,10)

        self.rect_4 = pygame.Rect(154,528,7,132.9)

        self.rect_5 = pygame.Rect(153,362,8,132.9)

        self.rect_6 = pygame.Rect(120,318,85,10)

        self.rect_7 = pygame.Rect(154.5,277,130,10)

        self.rect_8 = pygame.Rect(120,235,125,10)

        self.rect_9 = pygame.Rect(154,193,49,10)

        self.rect_10 = pygame.Rect(154,145,8,49)

        self.rect_11 = pygame.Rect(120,110,1200,10)

        self.rect_12 = pygame.Rect(196,120,7,73)
        
        self.rect_13 = pygame.Rect(238,120,7,115)

        self.rect_14 = pygame.Rect(280,120,7,165.5)

        self.rect_15 = pygame.Rect(238,280,7,89)

        self.rect_16 = pygame.Rect(238,402.5,7,218)

        self.rect_17 = pygame.Rect(196,360,7,300)
        
        self.rect_18 = pygame.Rect(155,485,45,10)

        self.rect_19 = pygame.Rect(154,736,7,133)

        self.rect_20 = pygame.Rect(320,277,90,10)

        self.rect_21 = pygame.Rect(280,235,132,10)

        self.rect_22 = pygame.Rect(322,194,132,10)

        self.rect_23 = pygame.Rect(405,150,90,10)

        self.rect_24 = pygame.Rect(488,150,7,50)

        self.rect_25 = pygame.Rect(405,150,7,50)

        self.rect_26 = pygame.Rect(530,120,7,123)

        self.rect_27 = pygame.Rect(363,120,7,40)

        self.rect_28 = pygame.Rect(321,150,7,51)

        self.rect_29 = pygame.Rect(240,403,129,8)

        self.rect_30 = pygame.Rect(200,361,129,8)

        self.rect_31 = pygame.Rect(240,319,129,8)

        self.rect_32 = pygame.Rect(326,194,83,8)

        self.rect_33 = pygame.Rect(362,325,7,84)
        
        self.rect_34 = pygame.Rect(405,280,7,172)

        self.rect_35 = pygame.Rect(405,486,7,256)

        self.rect_36 = pygame.Rect(279,445,130,8)

        self.rect_37 = pygame.Rect(363,486,173,8)

        self.rect_38 = pygame.Rect(321,736,216,8)

        self.rect_39 = pygame.Rect(154,695,216,8)

        self.rect_40 = pygame.Rect(200,653,128,8)

        self.rect_41 = pygame.Rect(240,611,88,8)

        self.rect_42 = pygame.Rect(155,736,90,8)

        self.rect_43 = pygame.Rect(196,778,48,8)

        self.rect_44 = pygame.Rect(116,903,900,8)

        self.rect_45 = pygame.Rect(155,820,130,8)

        self.rect_46 = pygame.Rect(195,862,50,8)

        self.rect_47 = pygame.Rect(279,862,90,8)

        self.rect_48 = pygame.Rect(279,700,7,85)

        self.rect_49 = pygame.Rect(279,820,7,42)

        self.rect_50 = pygame.Rect(238,785,6.5,42)

        self.rect_51 = pygame.Rect(196,865,7,42)

        self.rect_52 = pygame.Rect(362,740,7,46)

        self.rect_53 = pygame.Rect(363,490,7,170)

        self.rect_54 = pygame.Rect(279,450,7,127)

        self.rect_55 = pygame.Rect(321,480,7,95)

        self.rect_56 = pygame.Rect(280,570,47,8)

        self.rect_57 = pygame.Rect(321,616,7,43)

        self.rect_58 = pygame.Rect(446,445,7,49)
        
        self.rect_59 = pygame.Rect(446,195,7,48)
        
        self.rect_60 = pygame.Rect(446,280,7,128)

        self.rect_61 = pygame.Rect(410,360,40,8)

        self.rect_62 = pygame.Rect(280,778,48,8)

        self.rect_63 = pygame.Rect(320,820,170,8)

        self.rect_64 = pygame.Rect(529,820,132,8)

        self.rect_65 = pygame.Rect(321,780,7,48)

        self.rect_66 = pygame.Rect(404,778,7,90)

        self.rect_67 = pygame.Rect(446,528,7,174)

        self.rect_68 = pygame.Rect(488,780,7,90)

        self.rect_69 = pygame.Rect(446,860,7,50)

        self.rect_70 = pygame.Rect(530,743,7,125)

        self.rect_71 = pygame.Rect(410,778,43,8)

        self.rect_72 = pygame.Rect(490,861,43,8)

        self.rect_73 = pygame.Rect(490,194,43,8)

        self.rect_74 = pygame.Rect(447,236,43,8)

        self.rect_75 = pygame.Rect(447,403,89,8)

        self.rect_76 = pygame.Rect(447,528,89,8)

        self.rect_77 = pygame.Rect(447,695,89,8)

        self.rect_78 = pygame.Rect(488,200,7,170)

        self.rect_79 = pygame.Rect(488,410,7,42)

        self.rect_80 = pygame.Rect(488,570,7,90)

        self.rect_81 = pygame.Rect(495,570,250,8)

        self.rect_82 = pygame.Rect(495,278,290,8)

        self.rect_83 = pygame.Rect(530,405,7,83)

        self.rect_84 = pygame.Rect(530,613,7,86)

        self.rect_85 = pygame.Rect(572,152,90,8)

        self.rect_86 = pygame.Rect(571,120,7,40)

        self.rect_87 = pygame.Rect(571,196,7,90)

        self.rect_88 = pygame.Rect(571,319,7,50)

        self.rect_89 = pygame.Rect(571,403,7,132)

        self.rect_90 = pygame.Rect(571,570,7,48)

        self.rect_91 = pygame.Rect(571,653,7,91)

        self.rect_92 = pygame.Rect(571,862,7,46)

        self.rect_93 = pygame.Rect(571,862,48,8)

        self.rect_94 = pygame.Rect(571,778,132,8)

        self.rect_95 = pygame.Rect(696,778,7,50)

        self.rect_96 = pygame.Rect(490,361,85,8)

        self.rect_97 = pygame.Rect(530,320,130,8)

        self.rect_98 = pygame.Rect(573,194,86,8)

        self.rect_99 = pygame.Rect(655,236,90,8)

        self.rect_100 = pygame.Rect(655,196,7,44)

        self.rect_101 = pygame.Rect(655,824,7,44)

        self.rect_102 = pygame.Rect(613,824,7,44)
        
        self.rect_103 = pygame.Rect(613,611,7,170)

        self.rect_104 = pygame.Rect(613,487,7,86)

        self.rect_105 = pygame.Rect(613,362,7,43)

        self.rect_106 = pygame.Rect(613,235,7,85)

        self.rect_107 = pygame.Rect(656,861,47,8)

        self.rect_108 = pygame.Rect(574,653,40,8)

        self.rect_109 = pygame.Rect(530,611,42,8)

        self.rect_110 = pygame.Rect(573,403,130,8)

        self.rect_111 = pygame.Rect(573,445,88,8)

        self.rect_112 = pygame.Rect(615,611,130,8)

        self.rect_113 = pygame.Rect(904,445,8,460)

        self.rect_114 = pygame.Rect(904,120,8,290)

        self.rect_115 = pygame.Rect(696,120,7,82)

        self.rect_116 = pygame.Rect(863,120,7,123)

        self.rect_117 = pygame.Rect(738,153,7,84)

        self.rect_118 = pygame.Rect(822,153,7,130)

        self.rect_119 = pygame.Rect(780,195,7,130)

        self.rect_120 = pygame.Rect(745,152,80,8)

        self.rect_121 = pygame.Rect(740,402,85,8)

        self.rect_122 = pygame.Rect(737,319,90,8)

        self.rect_123 = pygame.Rect(700,361,127,8)

        self.rect_124 = pygame.Rect(696,320,7,174)

        self.rect_125 = pygame.Rect(738,405,7,90)

        self.rect_126 = pygame.Rect(655,445,7,90)

        self.rect_127 = pygame.Rect(655,322,7,46)

        self.rect_128 = pygame.Rect(822,322,7,46)

        self.rect_129 = pygame.Rect(863,280,7,46)

        self.rect_130 = pygame.Rect(863,360,7,49)

        self.rect_131 = pygame.Rect(780,445,7,215)

        self.rect_132 = pygame.Rect(738,528,7,85)

        self.rect_133 = pygame.Rect(821,403,7,133)

        self.rect_134 = pygame.Rect(865,320,40,8)

        self.rect_135 = pygame.Rect(822,278,45,8)

        self.rect_136 = pygame.Rect(822,444,48,8)

        self.rect_137 = pygame.Rect(869,402,42,8)

        self.rect_138 = pygame.Rect(660,528,80,8)

        self.rect_139 = pygame.Rect(655,653,125,8)

        self.rect_140 = pygame.Rect(785,570,85,8)

        self.rect_141 = pygame.Rect(780,736,130,8)

        self.rect_142 = pygame.Rect(739,861,130,8)

        self.rect_143 = pygame.Rect(821,570,7,90)

        self.rect_144 = pygame.Rect(863,450,7,120)
        
        self.rect_145 = pygame.Rect(780,695,7,130)

        self.rect_146 = pygame.Rect(738,695,7,170)

        self.rect_147 = pygame.Rect(821,770,7,92)

        self.rect_148 = pygame.Rect(654,655,7,88)

        self.rect_149 = pygame.Rect(654,736,48,8)

        self.rect_150 = pygame.Rect(695,695,48,8)

        self.rect_151 = pygame.Rect(822,695,48,8)

        self.rect_152 = pygame.Rect(822,653,48,8)

        self.rect_153 = pygame.Rect(863,820,48,8)

        self.rect_154 = pygame.Rect(863,611,48,8)

        self.rect_155 = pygame.Rect(739,820,48,8)

        self.rect_156 = pygame.Rect(696,700,7,43)

        self.rect_157 = pygame.Rect(863,654,7,43)

        self.rect_158 = pygame.Rect(863,778,7,45)

        self.finish = pygame.Rect(915,390,70,70)









        self.a = [self.rect_1, self.rect_2, self.rect_3, self.rect_4, self.rect_5, self.rect_6 ,self.rect_7, self.rect_8, self.rect_9, self.rect_10 ,self.rect_11 ,self.rect_12 ,self.rect_13 ,self.rect_14 ,self.rect_15 ,self.rect_16, self.rect_17, self.rect_18, self.rect_19, self.rect_20, self.rect_21, self.rect_22, self.rect_23, self.rect_24, self.rect_25, self.rect_26, self.rect_27, self.rect_28, self.rect_29, self.rect_30, self.rect_31, self.rect_32, self.rect_33, self.rect_34, self.rect_35, self.rect_36, self.rect_37, self.rect_38, self.rect_39, self.rect_40, self.rect_41, self.rect_42, self.rect_43, self.rect_44, self.rect_45, self.rect_46, self.rect_47, self.rect_48, self.rect_49, self.rect_50, self.rect_51, self.rect_52, self.rect_53, self.rect_54, self.rect_55, self.rect_56, self.rect_57, self.rect_58, self.rect_59, self.rect_60, self.rect_61, self.rect_62, self.rect_63, self.rect_64, self.rect_65, self.rect_66, self.rect_67, self.rect_68, self.rect_69, self.rect_70, self.rect_71, self.rect_72, self.rect_73, self.rect_74, self.rect_75, self.rect_76, self.rect_77, self.rect_78, self.rect_79, self.rect_80, self.rect_81, self.rect_82, self.rect_83, self.rect_84, self.rect_85, self.rect_86, self.rect_87, self.rect_88, self.rect_89, self.rect_90, self.rect_91, self.rect_92, self.rect_93, self.rect_94, self.rect_9, self.rect_96, self.rect_97, self.rect_98, self.rect_99, self.rect_100, self.rect_101, self.rect_102, self.rect_103, self.rect_104, self.rect_105, self.rect_106, self.rect_107, self.rect_108, self.rect_109, self.rect_110, self.rect_111, self.rect_112, self.rect_113, self.rect_114, self.rect_115, self.rect_116, self.rect_117, self.rect_118, self.rect_119, self.rect_120, self.rect_121, self.rect_122, self.rect_123, self.rect_124, self.rect_125, self.rect_126, self.rect_127, self.rect_128, self.rect_129, self.rect_130, self.rect_131, self.rect_132, self.rect_133, self.rect_134, self.rect_135, self.rect_136, self.rect_137, self.rect_138, self.rect_139, self.rect_140, self.rect_141, self.rect_142, self.rect_143, self.rect_144, self.rect_145, self.rect_146, self.rect_147, self.rect_148, self.rect_149, self.rect_150, self.rect_151, self.rect_152, self.rect_153, self.rect_154, self.rect_155, self.rect_156, self.rect_157, self.rect_158, self.finish]


    def draw_greed(self, screen, colour, rect):
        pygame.draw.rect(screen, colour, rect)
