from database import Database
from forumModel import forumModel
from cli import ForumCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.238.28.157:7687", "neo4j", "appearances-balloons-scrap")


myForumModel = forumModel(db)
myForumCLI = ForumCLI(myForumModel)
myForumCLI.run()
