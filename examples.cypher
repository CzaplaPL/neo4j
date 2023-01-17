//01. CALL db.schema.visualization()
CALL db.schema.visualization()

//02 MATCH r  = ()
MATCH r  = ()
RETURN r
LIMIT 10

//03 MATCH  (r)
MATCH  (r)
RETURN r
LIMIT 10

//04 MATCH  (r:City)
MATCH  (r:City)
RETURN r
LIMIT 10

//05 MATCH  p = (r:City)-[]-()
MATCH  p = (r:City)-[]-()
RETURN p
LIMIT 10

//06 MATCH  p = (r:City)-[]->()
MATCH  p = (r:City)-[]->()
RETURN p
LIMIT 10

//07 MATCH  p = (s :Store)-[:IN_STORE]-()
MATCH  p = (s :Store)-[:IN_STORE]-()
RETURN p
LIMIT 20

//08 MATCH  p = (s :City {name:"Tacoma"})-[:IN_CITY]-(:Store)
MATCH  p = (s :City {name:"Tacoma"})-[:IN_CITY]-(:Store)
RETURN p
LIMIT 20

//09 MATCH  p = (s :City {name:"Tacoma"})-[:IN_CITY]-(:Store)-[:IN_STORE]-()
MATCH  p = (s :City {name:"Tacoma"})-[:IN_CITY]-(:Store)-[:IN_STORE]-()
RETURN p


//10 MATCH (s:Sale)-[z :LINE_ITEM]-(p :Product)
MATCH (s:Sale)-[z :LINE_ITEM]-(p :Product)
RETURN s.id, z.price, p.name
LIMIT 10

//11 MATCH (s:Sale)-[z :LINE_ITEM]-(p :Product)
MATCH (s:Sale)-[z :LINE_ITEM]-(p :Product)
WHERE z.price > 80000 AND p.name <> "Washington Berry Juice"
RETURN s.id, z.price, p.name
LIMIT 10

//12 MATCH (p :Product)-[z :LINE_ITEM]-()
MATCH (p :Product)-[z :LINE_ITEM]-()
WHERE  p.name = "Washington Berry Juice"
RETURN  avg(z.price), p.name
LIMIT 10

//13MATCH (p :Product)-[z :LINE_ITEM]-(c)
MATCH (p :Product)-[z :LINE_ITEM]-(c)
WHERE  p.name = "Washington Berry Juice"
RETURN  *
ORDER by z.quantity

//14 MATCH (d:Date)-[:ON_DATE]-(s:Sale)
MATCH (d:Date)-[:ON_DATE]-(s:Sale)
WHERE d.date = "1997-01-02"
WITH s as wszytstkie_tranzakcje, d

MATCH (p:Promotion)--(g:Sale)-[:ON_DATE]->(d)
WITH wszytstkie_tranzakcje,d,g,p

MATCH (wszytstkie_tranzakcje)-[item :LINE_ITEM]-(p1:Product)
WITH wszytstkie_tranzakcje,d,g,p,item,p1


MATCH (g)-[item2 :LINE_ITEM]-(p2:Product)
WITH wszytstkie_tranzakcje,d,g,item,item2,p,p1,p2

RETURN *




//15 MATCH (d:Date)-[:ON_DATE]-(s:Sale)
MATCH (d:Date)-[:ON_DATE]-(s:Sale)
WHERE d.date = "1997-01-02"
WITH s as wszytstkie_tranzakcje, d

MATCH (p:Promotion)--(g:Sale)-[:ON_DATE]->(d)
WITH wszytstkie_tranzakcje,d,g,p

MATCH (wszytstkie_tranzakcje)-[item :LINE_ITEM]-(p1:Product)
WITH wszytstkie_tranzakcje,d,g,p,item,p1


MATCH (g)-[item2 :LINE_ITEM]-(p2:Product)
WITH wszytstkie_tranzakcje,d,g,item,item2,p,p1,p2

RETURN avg(item.price),avg(item2.price)