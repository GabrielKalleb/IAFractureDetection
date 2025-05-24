# DetectAI: Sistema de Detecção de Fraturas Ósseas em Raio-X

Utilizando redes neurais profundas, este sistema identifica fraturas ósseas em imagens radiográficas com alta precisão. Desenvolvido para auxiliar profissionais de saúde, o modelo foi treinado em um dataset diversificado e balanceado, garantindo robustez em diferentes cenários clínicos.

## 📁 Base de Dados

O treinamento utilizou o dataset público Fracture Multi-Region X-Ray Data, disponível no Kaggle:

🔗 **Acessar Dataset:** [Fracture Multi-Region X-Ray Data](https://www.kaggle.com/datasets/bmadushanirodrigo/fracture-multi-region-x-ray-data)

### Detalhes do Conjunto de Dados:
* **Imagens de treinamento:** 9.246
* **Imagens de validação:** 828
* **Imagens de teste:** 506

### Fontes Originais:
* Bone Break Classifier Dataset (Mohan Kumar)
* bone_fracture (Abdelaziz Faramawy)
* fracture (Harsha Arya)

## 🛠 Funcionalidades Técnicas

* **Pré-processamento automático:** Redimensionamento, conversão para escala de cinza e normalização.
* **Predição em tempo real:** Processamento rápido para integração em fluxos de trabalho clínicos.
* **Saída interpretável:** Probabilidade clara (0 a 1) para decisão assistida.

## 📦 Estrutura do Projeto

Arquivos essenciais incluídos:

* `IAFractureDetection.ipynb`: Script para treinar o modelo a partir do dataset.
* `predict_function.py`: Funções para pré-processamento e inferência.

## 🩺 Como Utilizar o Sistema

### Pré-processamento:
1.  Carregue a imagem em formato `.jpg` ou `.png`.
2.  A imagem é convertida para `223x223` pixels em escala de cinza.
3.  Valores normalizados entre `0` e `1`.

### Execução da Predição:
* O modelo retorna um valor entre `0` (normal) e `1` (fratura detectada).
* **Limiar de decisão:** `0.5` (acima indica fratura).

## 📊 Desempenho do Modelo

* **Acurácia Geral:** 94%
    *Métricas validadas em dados de teste independentes, com garantia de ausência de vazamento entre conjuntos.*

## ⚠ Observações Críticas

* **Formato da imagem:** Utilize radiografias em escala de cinza sem redimensionamento prévio.
* **Contexto clínico:** Resultados devem ser interpretados por profissionais qualificados.
* **Limitações:** O desempenho pode variar em casos atípicos ou imagens de baixa qualidade.

## 🚑 Nota de Responsabilidade

Este sistema é uma ferramenta de apoio diagnóstico e **não substitui avaliação médica completa**. Sempre confirme os resultados com exames complementares e análise especializada.
