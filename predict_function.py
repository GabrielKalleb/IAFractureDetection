import os
import numpy as np
import tensorflow as tf
import cv2

# Configurações
IMG_SIZE = 223

def preprocess_image(image_array):
  
    if len(image_array.shape) == 3 and image_array.shape[2] == 3:
        image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    image_array = image_array.astype(np.uint8)
    image_array = cv2.equalizeHist(image_array)
    image_array = cv2.GaussianBlur(image_array, (5, 5), 0)
    image_array = image_array.astype(np.float32) / 255.0
    image_array = cv2.resize(image_array, (IMG_SIZE, IMG_SIZE))
    image_array = np.expand_dims(image_array, axis=-1)
    image_array = np.expand_dims(image_array, axis=0)

    return image_array

def image_predict(model_path, preprocessed_image_array): # --> Para o pessoal do Back end
    modelo = tf.keras.models.load_model(model_path)
    print("Resumo do modelo carregado:")
    modelo.summary()
    predicao = modelo.predict(preprocessed_image_array)
    return predicao






#Teste da Predição
def main():
    path_imagem_teste = 'caminho_da_imagem'
    path_modelo = 'caminho_do_modelo'
    if not os.path.exists(path_imagem_teste):
        print(f"Erro: Imagem de teste não encontrada em '{path_imagem_teste}'")
        return
    if not os.path.exists(path_modelo):
        print(f"Erro: Modelo não encontrado em '{path_modelo}'")
        return
    imagem_original = cv2.imread(path_imagem_teste, cv2.IMREAD_GRAYSCALE)

    if imagem_original is None:
        print(f"Erro ao carregar a imagem: {path_imagem_teste}")
        return
    imagem_preprocessada = preprocess_image(imagem_original)
    print(f"Shape da imagem após pré-processamento: {imagem_preprocessada.shape}")


    # Fazer a predição
    predicao_imagem = image_predict(path_modelo, imagem_preprocessada)
    if predicao_imagem is not None:
        print("\nPredição (valor bruto):", predicao_imagem)
        if predicao_imagem[0][0] > 0.5:
            print("Resultado: Não Fraturado (Classe 1)")
        else:
            print("Resultado: Fraturado (Classe 0)")

if __name__ == '__main__':
    main()