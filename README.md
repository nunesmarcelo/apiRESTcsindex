# API REST - MARCELO NUNES DA SILVA 2017023560


## Introdução: 

 Este documento visa apresentar informações sobre a API para filtragens de informações do sistema CSIndex(http://csindexbr.org/) construída utilizando a arquitetura REST. 
 Para que as consultas sejam realizadas foram realizadas consultas às planilhas presentes na pasta "data" do projeto, pré fornecidas pelo professor.

## Esclarecimentos Importantes

 O uso de APIs REST tem como princípio o fato de se enviar requisições a um "provedor" que irá processar o que foi requisitado, e retornar uma resposta, de acordo com o que foi solicitado. Para se obter dados, o padrão é se realizar a solicitação via GET, o cadastrado de dados é feito via POST, alteração com PUT/PATCH e para deletar, o DELETE é usado.
 Como esse projeto utiliza requisições para receber dados, o método ao qual se devem ser enviadas as requisições é o método **GET**.


## Documentação - Para se realizar cada uma das consultas

### 1- Número de publicações em uma determinada conferência de uma área 
  Passar um campo com a {area} que corresponde à area pesquisada, e outro campo com a {conferência}, que corresponde à conferência buscada, e a API responderá à requisição efetuada com um csv.
  
  > GET /buscar_conferencia_por_area/{area}/{conferência}
  
#### Exemplos de uso (rode o projeto para que o servidor possa receber à requisição, e o link irá funcionar, por executar essa requisição como GET):

  1º - [http://127.0.0.1:5000/buscar_conferencia_por_area/ir/WWW](http://127.0.0.1:5000/buscar_conferencia_por_area/ir/WWW)
  
  2º - [http://127.0.0.1:5000/buscar_conferencia_por_area/pl/GPCE](http://127.0.0.1:5000/buscar_conferencia_por_area/pl/GPCE)
<hr>



 ### 2- Número de publicações no conjunto de conferências de uma área 
  Passar um campo com a {area} que corresponde à area pesquisada, e a API responderá à requisição efetuada com um csv.
  
  > GET /buscar_todas_conferencias_area/{area}
  
#### Exemplos de uso (rode o projeto para que o servidor possa receber à requisição, e o link irá funcionar, por executar essa requisição como GET):

  1º - [http://127.0.0.1:5000/buscar_todas_conferencias_area/security](http://127.0.0.1:5000/buscar_todas_conferencias_area/security)
  
  2º - [http://127.0.0.1:5000/buscar_todas_conferencias_area/theory](http://127.0.0.1:5000/buscar_todas_conferencias_area/theory)
  
  <hr>
  
  
  ### 3- Scores de todos os departamentos em uma área
   Passar um campo com a {area} que corresponde à area pesquisada, e a API responderá à requisição efetuada com um csv.
  
  > GET /scores_departamentos_uma_area/{area}
  
#### Exemplos de uso (rode o projeto para que o servidor possa receber à requisição, e o link irá funcionar, por executar essa requisição como GET):

  1º - [http://127.0.0.1:5000/scores_departamentos_uma_area/se](http://127.0.0.1:5000/scores_departamentos_uma_area/se)
  
  2º - [http://127.0.0.1:5000/scores_departamentos_uma_area/vision](http://127.0.0.1:5000/scores_departamentos_uma_area/vision)
  
  <hr>
  
  
  
  ### 4- Score de um determinado departamento em uma área
   Passar um campo com a {area} que corresponde à area pesquisada, e o nome do {departamento} buscado, e a API responderá à requisição efetuada com um csv.
  
  > GET /score_departamento_uma_area/{area}/{departamento}
  
#### Exemplos de uso (rode o projeto para que o servidor possa receber à requisição, e o link irá funcionar, por executar essa requisição como GET):

  1º - [http://127.0.0.1:5000/score_departamento_uma_area/ai/UFPE](http://127.0.0.1:5000/score_departamento_uma_area/ai/UFPE)
  
  2º - [http://127.0.0.1:5000/score_departamento_uma_area/se/UFMG](http://127.0.0.1:5000/score_departamento_uma_area/se/UFMG)
  
  <hr>
  
 
   ### 5- Número de professores que publicam em uma determinada área (organizados por departamentos)
   Passar um campo com a {area} que corresponde à area pesquisada, e a API responderá à requisição efetuada com um csv.
  
  > GET /professores_departamento_uma_area/{area}
  
#### Exemplos de uso (rode o projeto para que o servidor possa receber à requisição, e o link irá funcionar, por executar essa requisição como GET):

  1º - [http://127.0.0.1:5000/professores_departamentos_uma_area/ai](http://127.0.0.1:5000/professores_departamentos_uma_area/ai)
  
  2º - [http://127.0.0.1:5000/professores_departamentos_uma_area/chi](http://127.0.0.1:5000/professores_departamentos_uma_area/chi)
  
  <hr>
  
  
   ### 6- Número de professores de um determinado departamento que publicam em uma área
   Passar um campo com a {area} que corresponde à area pesquisada, e o nome do {departamento} buscado, e a API responderá à requisição efetuada com um csv.
  
  > GET /professores_departamentos_uma_area/{area}/{departamento}
  
#### Exemplos de uso (rode o projeto para que o servidor possa receber à requisição, e o link irá funcionar, por executar essa requisição como GET):

  1º - [http://127.0.0.1:5000/professores_departamento_uma_area/se/UFMG](http://127.0.0.1:5000/professores_departamento_uma_area/se/UFMG)
  
  2º - [http://127.0.0.1:5000/professores_departamento_uma_area/arch/UFBA](http://127.0.0.1:5000/professores_departamento_uma_area/arch/UFBA)
  
  <hr>
  
  
   ### 7- Todos os papers de uma área (ano, título, deptos e autores)
   Passar um campo com a {area} que corresponde à area pesquisada, e a API responderá à requisição efetuada com um csv.
  
  > GET /papers_uma_area/{area}
  
#### Exemplos de uso (rode o projeto para que o servidor possa receber à requisição, e o link irá funcionar, por executar essa requisição como GET):

  1º - [http://127.0.0.1:5000/papers_uma_area/formal](http://127.0.0.1:5000/papers_uma_area/formal)
  
  2º - [http://127.0.0.1:5000/papers_uma_area/db](http://127.0.0.1:5000/papers_uma_area/db)
  
  <hr>
  
  
   ### 8- Todos os papers de uma área em um determinado ano
   Passar um campo com a {area} que corresponde à area pesquisada, e o {ano} buscado, e a API responderá à requisição efetuada com um csv.
  
  > GET /papers_uma_area_ano/{area}/{ano}
  
#### Exemplos de uso (rode o projeto para que o servidor possa receber à requisição, e o link irá funcionar, por executar essa requisição como GET):

  1º - [http://127.0.0.1:5000/papers_uma_area_ano/ds/2017](http://127.0.0.1:5000/papers_uma_area_ano/ds/2017)
  
  2º - [http://127.0.0.1:5000/papers_uma_area_ano/formal/2014](http://127.0.0.1:5000/papers_uma_area_ano/formal/2014)
  
  <hr>
  
   
   ### 9- Todos os papers de um departamento em uma área
   Passar um campo com a {area} que corresponde à area pesquisada, e o {departamento} buscado, e a API responderá à requisição efetuada com um csv.
  
  > GET /papers_uma_area_departamento/{area}/{departamento}
  
#### Exemplos de uso (rode o projeto para que o servidor possa receber à requisição, e o link irá funcionar, por executar essa requisição como GET):

  1º - [http://127.0.0.1:5000/papers_uma_area_departamento/ir/UFMG](http://127.0.0.1:5000/papers_uma_area_departamento/ir/UFMG)
  
  2º - [http://127.0.0.1:5000/papers_uma_area_departamento/is/UFES](http://127.0.0.1:5000/papers_uma_area_departamento/is/UFES)
  
  <hr>
  

    
   ### 10- Todos os papers de um professor (dado o seu nome)
   Passar um campo com a {area} que corresponde à area pesquisada, e o {nome} buscado, e a API responderá à requisição efetuada com um csv.
  
  > GET /papers_uma_area_autor/{area}/{autor}
  
#### Exemplos de uso (rode o projeto para que o servidor possa receber à requisição, e o link irá funcionar, por executar essa requisição como GET):

  1º - [127.0.0.1:5000/papers_uma_area_autor/se/Marco Tulio Valente](http://127.0.0.1:5000/papers_uma_area_autor/se/Marco%20Tulio%20Valente)
  
  2º - [127.0.0.1:5000/papers_uma_area_autor/vision/Jefersson A. dos Santos](http://127.0.0.1:5000/papers_uma_area_autor/vision/Jefersson%20A.%20dos%20Santos)
  
  
