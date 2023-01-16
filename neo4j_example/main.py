from neo4j import GraphDatabase, ServerInfo, Session

URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "password")


def print_connection_details(info: ServerInfo) -> None:
    print(f"Connection info: agent={info.agent} address={info.address} protocol_version={info.protocol_version}")


def print_all_nodes(session: Session) -> None:
    count = session.run("""
        MATCH ()
        RETURN COUNT(*) as count
    """).single()
    result = session.run("""
        MATCH (s)
        RETURN s
    """).fetch(10)
    print(f"Nodes count: {count.data()['count']}")
    for item in result:
        print(item.data())


def add_new_nodes(session: Session) -> None:
    test = session.run("""
            CREATE (s1:Student {fullname: "Kacper Czajkowski", birthdate: "1999-11-19"}),
                (s2:Student {fullname: "Dominik Daniłowski", birthdate: "1998-04-17"}),
                (s3:Student {fullname: "Marcin Zadrożny", birthdate: "2000-08-21"}),
                (w:Wydzial {name: "Wydział Matematyki i Informatyki", abbreviation: "WMII"}),
                (s2) -[r1:STUDIUJE_NA]-> (w),
                (s3) -[r2:STUDIUJE_NA]-> (w)
            RETURN s1, s2, s3, w
        """).single()
    print(test.data())


def add_relationship_between_existing_nodes(session: Session) -> None:
    result = session.run("""
        MATCH (s:Student {fullname: "Kacper Czajkowski"}), (w:Wydzial {abberviation: "WMII"})
        CREATE (s) -[:STUDIUJE_NA]-> (w)
    """).single()


def add_or_update_property_in_node(session: Session) -> None:
    result = session.run("""
        MATCH (s:Student {fullname: "Kacper Czajkowski"})
        SET s.fullname = "Kacper Zedytowany Czajkowski"
    """).single()


def override_all_properties_of_node(session: Session) -> None:
    result = session.run("""
        MATCH (s:Student {fullname: "Dominik Daniłowski"})
        SET s = {full_name: "Henryk Daniłowski", age: 24}
    """).single()


def update_multiple_properties(session: Session) -> None:
    result = session.run("""
        MATCH (s:Student {fullname: "Marcin Zadrożny"})
        SET s += {fullname: "Marcin Odświeżony Zadrożny", age: 23}
    """).single()


# usuwanie
# usuwanie node'a
# usuwanie property
# usuwanie labela ze wszystkich node'ów
# usuwanie wszystkiego
def remove_all_nodes_and_relationships(session: Session) -> None:
    session.run("""
        MATCH (n)
        DETACH DELETE n;
    """).single()


if __name__ == '__main__':
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        print_connection_details(driver.get_server_info())
        with driver.session() as session:
            remove_all_nodes_and_relationships(session)
            print_all_nodes(session)
            add_new_nodes(session)
            print_all_nodes(session)
            add_relationship_between_existing_nodes(session)
            print_all_nodes(session)
            update_multiple_properties(session)
            print_all_nodes(session)
            override_all_properties_of_node(session)
            print_all_nodes(session)
