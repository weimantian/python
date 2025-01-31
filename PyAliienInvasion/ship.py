import pygame

class Ship:

	def __init__(self, ai_game):
		"""初始化飞船，并设置其初始化位置"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# 加载飞船图像并获取起外接矩形
		self.image = pygame.image.load('images/ship.png')
		self.rect = self.image.get_rect()

		#对于每艘新飞船都将起=其放到屏幕底部的中中央
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)