# Herança e Duck Typing

A1/A2  - Criando Playlist / reaproveitando um list:

	É possível reaproveitar objetos prontos no python dentro de outros objetos, para isso basta herdar as propriedades como em:
	
		class playList(list):
		    def __init__(self, playlistName,listaProgramas) :
		        self.__name = playlistName
		        super().__init__(listaProgramas)
	
	O super é necessário para utilizar o construtor de list com algumas propriedades extras.
	
A3 - Fugindo da complexidade

O ideal é sempre evitar realizar herança de métodos que você não conhece totalmente.


<h3>Duck Typing</h3>
![image](https://user-images.githubusercontent.com/75864813/130531785-04250971-ec31-498b-8342-b670322ce95e.png)

