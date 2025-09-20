# Carbonate - Petrobras - ucarbon

Este repositório contêm fluxos de trabalho iniciais do projeto  

This repo has initial workflows from the project***Avanços na metodologia de datação U-Pb em rochas sedimentares aplicado as bacias brasileiras***, sponsored by Petrobras (2024/00561-7).

## Requirements

### Projeto: contexto e objetivo

> A datação in situ de minerais com baixo teor de urânio, especialmente de fases carbonáticas, vem se consolidando como importante ferramenta na investigação de eventos sedimentares e de sua relação com a qualidade de reservatórios. Avanços recentes na datação urânio-chumbo (U-Pb) de carbonatos se beneficiaram do aumento da capacidade de detecção dos espectrômetros de massa associados à amostragem por ablação por laser. Contudo, o entendimento dos controles texturais e composicionais na qualidade dos dados geocronológicos ainda é limitado. Para abordar essa questão, pretende-se desenvolver um sistema computacional que integrará resultados de datações, imagens petrográficas, imagens e dados espectrais obtidos por catodoluminescência e por sensores hiperespectrais, imagens e dados composicionais obtidos por microscopia eletrônica de varredura, microfluorescência de raios X, mapeamento composicional com espectrômetro de massas e métodos que utilizam luz síncrotron. Esse sistema deverá permitir a visualização e análise de dados organizados em camadas e associados a redução de dados geocronológicos. Assim, pretende-se viabilizar a avaliação de cada ponto de ablação por laser e sua contribuição à datação, considerando aspectos composicionais e texturais obtidos por diversas técnicas. Espera-se com isso maximizar a robustez dos resultados e alcançar a sinergia entre a petrologia e a geocronologia aplicadas a rochas  sedimentares. Para otimizar a seleção de alvos para datação, serão aplicados algoritmos de análise estatística multivariada para detecção de correlações entre características composicionais, texturais e diagenéticas associadas a variação da qualidade dos resultados geocronológicos. Outros proxies, incluindo isótopos de estrôncio e distribuição de elementos terras raras, também serão integrados na análise proposta e na investigação de sequências paragenéticas. Em paralelo, incrementos em acurácia e precisão dos resultados geocronológicos serão buscados por meio de ajustes finos de parâmetros de aquisição e estabelecimento de novos materiais de referência. A investigação dos parâmetros de aquisição e a validação dos resultados obtidos contará com análises em diferentes equipamentos, envolvendo ampla rede de parceiros internacionais.


### Data and Sensors

1. Espera-se que a aplicação processe dados de:
  * **geochronological dating/ages**
  * **photomicrographs**
  * spectral image and data by **cathodoluminescence** and by **hiperespectral sensors**
  * **EMPA** compositional maps
  * **X-ray microfluorescence**
  * compositional map with **mass spectometer**
  * sincroton light

### Software

Some software is already available.

* XMapTools
  * compositional maps and spots
  * SEM
  * EMPA
  * LA-ICP-MS
  * CT-Scanner
* Python
  * data: pandas, numpy, scipy, 
  * dataviz: seaborn, matplotlib, plotly
  * images: openCV, rasterio


### Scope

## This repo

### 1. Carregamento

### 2. The resolution problema
  
#### upscale
  * `NEAREST`
  * `LINEAR`
  * `CUBIC`
  * `LANCZOS4`
#### downscale
  * `INTERAREA`

### 3. The coordinate problem

  * Align images using openCV?
  * When putting together Spot and Maps, a correlation approach similar to XMapTools might work.
    * an adjustable correlation matrix where color ramp indicates the correlation between spot and map
    * the matrix map shows which pixel has higher correlation 

### 4. EDA

### 5. Modelling

### 6. Outputs
