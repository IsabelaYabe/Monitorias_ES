A atividade consiste em aplicar os padrões de projeto Abstract Factory, Factory Method e Singleton por meio da criação de um framework para visualização de arquivos. Esse framework deve fornecer uma interface gráfica capaz de ser utilizada tanto no sistema Windows quanto no Mac, garantindo que cada sistema operacional possua sua própria aparência, incluindo janela e cursor personalizados.

Além disso, o framework deve assegurar que apenas uma instância da aplicação possa ser executada por vez, utilizando o padrão Singleton para controlar a criação da aplicação principal. O padrão Abstract Factory será responsável por criar as famílias de objetos relacionadas à interface, permitindo múltiplas implementações, uma voltada para o Windows e outra para o Mac. Já o padrão Factory Method será empregado na criação dos documentos ou arquivos que serão visualizados dentro da aplicação.

O resultado esperado é um sistema capaz de criar e abrir arquivos por meio do Factory Method, renderizar janelas e cursores de acordo com o sistema operacional através do Abstract Factory, e impedir a execução simultânea de múltiplas instâncias da aplicação utilizando o Singleton.

Para testar rode: 
python -m atividade_0.main