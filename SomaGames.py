import streamlit as st
from molde import molde_game, molde_raio

def somar_game(placar):
   placar = placar.split("\n")
   placar = [''.join([x for x in rodada if x in '❤️💚💛💙']) for rodada in placar if len([x for x in rodada if x in '❤️💚💛💙']) > 1]
   resultados = []
   for x in placar:
      x = x.replace('❤️', 'G')
      x = x.replace('💛', 'L')
      x = x.replace('💙', 'C')
      x = x.replace('💚', 'S')
      resultados.append(x)
   placar_final = [['G', 0],['L', 0],['C', 0],['S', 0]]
   for x in range(4):
      for y in resultados:
         for z in y:
            if z == placar_final[x][0]:
               placar_final[x][1] += (8 - y.index(z)) * 10
   return [x[1] for x in placar_final]

def Main():
   st.title("Soma Games")
   st.text("por Luis Fernando Santos Cardeal")
   aplicacao = st.sidebar.radio("Tipo de aplicação", ["Game", "Raio"])
   if aplicacao == "Game":
      Game()
   elif aplicacao == "Raio":
      Raio()

def Game():
   st.subheader("Sobre o Jogo")
   aplicador = st.text_input("Nome do aplicador", placeholder="O Jogo - você perdeu")
   col1, col2 = st.columns(2)
   with col1:
      nome_game = st.text_input("Informe o nome do game")
   with col2:
      data_game = st.date_input("Informe a data de aplicação")
      data_game = "/".join(str(data_game).split("-")[::-1])
   st.subheader("Placar")
   #GRYFF
   st.markdown("### Gryff")
   colg1, colg2 = st.columns(2)
   with colg1:
      gryff_chamada = st.select_slider("Gryff - Chamada", [x * 10 for x in range(11)])
   with colg2:
      gryff_descontos = st.number_input("Gryff - Descontos", step = 10, min_value = 0)
   #HUFF
   st.markdown("### Huff")
   colh1, colh2 = st.columns(2)
   with colh1:
      huff_chamada = st.select_slider("Huff - Chamada", [x * 10 for x in range(11)])
   with colh2:
      huff_descontos = st.number_input("Huff - Descontos", step = 10, min_value = 0)
   #RAV
   st.markdown("### Raven")
   colr1, colr2 = st.columns(2)
   with colr1:
      raven_chamada = st.select_slider("Raven - Chamada", [x * 10 for x in range(11)])
   with colr2:
      raven_descontos = st.number_input("Raven - Descontos", step = 10, min_value = 0)
   #SLY
   st.markdown("### Sly")
   cols1, cols2 = st.columns(2)
   with cols1:
      sly_chamada = st.select_slider("Sly - Chamada", [x * 10 for x in range(11)])
   with cols2:
      sly_descontos = st.number_input("Sly - Descontos", step = 10, min_value = 0)
   st.markdown("### Placar")
   placar_game = st.text_area("Cole o placar aqui", height=200)

   molde = False
   if st.checkbox("Adicionar Molde"):
      molde = st.text_area("Insita seu molde")
   if st.button("Somar"):
      if not molde:
         molde = molde_game
      gryff_game, huff_game, raven_game, sly_game = somar_game(placar_game)
      gryff_total = gryff_game + gryff_chamada - gryff_descontos         
      huff_total = huff_game + huff_chamada - huff_descontos
      raven_total = raven_game + raven_chamada - raven_descontos
      sly_total = sly_game + sly_chamada - sly_descontos
      placar_final = f"{molde}".format(nome_game, aplicador, data_game, gryff_chamada, gryff_game, gryff_descontos, gryff_total, huff_chamada, huff_game, huff_descontos, huff_total, raven_chamada, raven_game, raven_descontos, raven_total, sly_chamada, sly_game, sly_descontos, sly_total)
      st.text_area("Placar Final", value = placar_final, height = 300)
      
def Raio():
   st.subheader("Sobre os Raios")
   aplicador = st.text_input("Nome do aplicador", placeholder="O Jogo - você perdeu")
   col1, col2 = st.columns(2)
   with col1:
      quant_raios = st.number_input("Informe a quantidade de raios aplicados", min_value=1, step=1)
   with col2:
      data_game = st.date_input("Informe a data de aplicação")
      data_game = "/".join(str(data_game).split("-")[::-1])
   st.subheader("Medalhas")

   #ÁREA DA GRYFF
   st.markdown("### Gryff")
   g1, g2, g3, g4 = st.columns(4)
   with g1:
      gryff_1 = st.number_input("Gryff - Primeiro Lugar", 0,  step = 1)
   with g2:
      gryff_2 = st.number_input("Gryff - Segundo Lugar", 0,  step = 1)
   with g3:
      gryff_3 = st.number_input("Gryff - Terceiro Lugar", 0,  step = 1)
   with g4:
      gryff_4 = st.number_input("Gryff - Quarto Lugar", 0,  step = 1)
   gryff_add = st.text_input("Gryff adicionais", help="Os valores adicionais são para os raios que valem mais que o normal", value="0")

   #ÁREA DA HUFF
   st.markdown("### Huff")
   h1, h2, h3, h4 = st.columns(4)
   with h1:
      huff_1 = st.number_input("Huff - Primeiro Lugar", 0,  step = 1)
   with h2:
      huff_2 = st.number_input("Huff - Segundo Lugar", 0,  step = 1)
   with h3:
      huff_3 = st.number_input("Huff - Terceiro Lugar", 0,  step = 1)
   with h4:
      huff_4 = st.number_input("Huff - Quarto Lugar", 0,  step = 1)
   huff_add = st.text_input("Huff adicionais", help="Os valores adicionais são para os raios que valem mais que o normal", value="0")

   #ÁREA DA RAVEN
   st.markdown("### Raven")
   r1, r2, r3, r4 = st.columns(4)
   with r1:
      raven_1 = st.number_input("Raven - Primeiro Lugar", 0,  step = 1)
   with r2:
      raven_2 = st.number_input("Raven - Segundo Lugar", 0,  step = 1)
   with r3:
      raven_3 = st.number_input("Raven - Terceiro Lugar", 0,  step = 1)
   with r4:
      raven_4 = st.number_input("Raven - Quarto Lugar", 0,  step = 1)
   raven_add = st.text_input("Raven adicionais", help="Os valores adicionais são para os raios que valem mais que o normal", value="0")

   #ÁREA DA SLY
   st.markdown("### Sly")
   s1, s2, s3, s4 = st.columns(4)
   with s1:
      sly_1 = st.number_input("Sly - Primeiro Lugar", 0, step = 1)
   with s2:
      sly_2 = st.number_input("Sly - Segundo Lugar", 0, step = 1)
   with s3:
      sly_3 = st.number_input("Sly - Terceiro Lugar", 0, step = 1)
   with s4:
      sly_4 = st.number_input("Sly - Quarto Lugar", 0, step = 1)
   sly_add = st.text_input("Sly adicionais", help="Os valores adicionais são para os raios que valem mais que o normal", value="0")

   if st.button("Somar"):
      molde = molde_raio
      
      gryff_raios = gryff_1 * 50 + gryff_2 * 40 + gryff_3 * 30 + gryff_4 * 20
      gryff_total = gryff_raios + int(gryff_add)

      huff_raios = huff_1 * 50 + huff_2 * 40 + huff_3 * 30 + huff_4 * 20
      huff_total = huff_raios + int(huff_add)

      raven_raios = raven_1 * 50 + raven_2 * 40 + raven_3 * 30 + raven_4 * 20
      raven_total = raven_raios + int(raven_add)

      sly_raios = sly_1 * 50 + sly_2 * 40 + sly_3 * 30 + sly_4 * 20
      sly_total = sly_raios + int(sly_add)

      placar_final = f"{molde}".format(aplicador, data_game, quant_raios, gryff_total, huff_total, raven_total, sly_total)
      st.text_area("Placar Final", value = placar_final, height = 300)

if __name__ == '__main__':
    Main()
