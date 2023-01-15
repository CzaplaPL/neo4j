from neo4j import GraphDatabase, ServerInfo, Session

URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "password")


def print_connection_details(info: ServerInfo) -> None:
    print(f"Connection info: agent={info.agent} address={info.address} protocol_version={info.protocol_version}")


def print_sales_count_from_date(session: Session) -> None:
    date: str = '1998-10-26'
    result = session.run(
        "MATCH (o:Sale) -[:ON_DATE]->(d:Date {date: $order_date}) RETURN count(o) as count_of_sales",
        order_date=date
    ).single()
    count = result.data()['count_of_sales']
    print(f'Sales count from day {date} is {count}.')


def print_ten_first_product_categories(session: Session) -> None:
    result = session.run("MATCH (pc: ProductCategory) RETURN pc").fetch(10)
    print('10 product categories:')
    for record in result:
        item = record.data()
        print('- ', item['pc']['name'])


# TODO implementacja
def add_new_customer(session: Session) -> None:
    # session.run("""
    #     CREATE
    # """)
    pass


# TODO implementacja
def add_relation_for_customer_and_region(session: Session) -> None:
    pass


# TODO implementacja
def update_customer_label(session: Session) -> None:
    pass


if __name__ == '__main__':
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        print_connection_details(driver.get_server_info())
        with driver.session() as session:
            print_ten_first_product_categories(session)
            print_sales_count_from_date(session)
