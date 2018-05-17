## API REST - MARCELO NUNES DA SILVA 2017023560


### Introdução: 

 Este documento visa apresentar informações sobre a API para filtragens de informações do sistema CSIndex(http://csindexbr.org/) construída utilizando a arquitetura REST. 
 Para que as consultas sejam realizadas foram realizadas consultas às planilhas presentes na pasta "data" do projeto, pré fornecidas pelo professor.

### Esclarecimentos Importantes

 O uso de APIs REST tem como princípio o fato de se enviar requisições a um "provedor" que irá processar o que foi requisitado, e retornar uma resposta, de acordo com o que foi solicitado. Para se obter dados, o padrão é se realizar a solicitação via GET, o cadastrado de dados é feito via POST, alteração com PUT/PATCH e para deletar, o DELETE é usado.
 Como esse projeto utiliza requisições para receber dados, o método ao qual se devem ser enviadas as requisições é o método **GET**.


### Documentação - Para se realizar cada uma das consultas

#### 1- Número de publicações em uma determinada conferência de uma área 
  Passar um campo com a {area} que corresponde à area pesquisada, e outro campo com a {conferência}, que corresponde à conferência buscada, e a API responderá à requisição efetuada com um csv.
  
  > GET /buscar_conferencia_por_area/{area}/{conferência}
  
##### Exemplos de uso (rode o projeto para que o servidor possa receber à requisição):

  1º - [http://127.0.0.1:5000/buscar_conferencia_por_area/ir/WWW](http://127.0.0.1:5000/buscar_conferencia_por_area/ir/WWW)
  
  2º - [http://127.0.0.1:5000/buscar_conferencia_por_area/pl/GPCE](http://127.0.0.1:5000/buscar_conferencia_por_area/pl/GPCE)
  
 #### 2- Número de publicações no conjunto de conferências de uma área 
  Passar um campo com a {area} que corresponde à area pesquisada, e a API responderá à requisição efetuada com um csv.
  
  > GET /buscar_todas_conferencias_area/{area}/
  
##### Exemplos de uso (rode o projeto para que o servidor possa receber à requisição):

  1º - [http://127.0.0.1:5000/buscar_todas_conferencias_area/security/](http://127.0.0.1:5000/buscar_todas_conferencias_area/security/)
  
  2º - [http://127.0.0.1:5000/buscar_todas_conferencias_area/theory/](http://127.0.0.1:5000/buscar_todas_conferencias_area/theory/)
