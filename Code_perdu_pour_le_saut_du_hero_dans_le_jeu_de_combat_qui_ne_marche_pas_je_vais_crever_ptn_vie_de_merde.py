'''            if self.hero.get_saut():
                if self.hero.get_pos_y() > 100:
                    self.hero.modif_pos_y(-(self.hero.get_pos_y()+100)/10)
                    
                else:
                    self.hero.set_saut(False)
            elif not self.hero.get_saut() and self.hero.get_pos_y() < 600:
                if self.hero.get_pos_y() >= 530:
                    self.hero.modif_pos_y(-self.hero.get_pos_y()+530)
                else:
                    self.hero.modif_pos_y(self.hero.get_pos_y()/8)'''