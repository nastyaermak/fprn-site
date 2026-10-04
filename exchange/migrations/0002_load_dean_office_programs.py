from django.db import migrations

UNIVERSITY_NAMES = [
    "Uniwersytet Warszawski",
    "KU Leuven",
    "Vilnius University",
    "Uniwersytet Jagielloński",
    "University of Tartu",
    "Masaryk University",
]

INSERT_SQL = """
INSERT INTO exchange_exchangeprogram (university, languages, places, deadline, description) VALUES
('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15',
 'Найбільший університет Польщі, заснований у 1816 році. Студенти обміну можуть обирати курси з біології, хімії та фізики польською або англійською мовою.'),
('KU Leuven (Бельгія)', 'English', '2 місця', '2026-12-01',
 'Один із найстаріших університетів Європи, заснований у 1425 році, і провідний дослідницький університет Бельгії. Для студентів обміну доступні англомовні курси з природничих наук.'),
('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20',
 'Найстаріший університет Литви, заснований у 1579 році. Студенти обміну навчаються на англомовних курсах з біохімії, екології та фізики.'),
('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15',
 'Найстаріший університет Польщі, заснований у Кракові в 1364 році. Факультети біології та хімії приймають студентів на семестрові програми обміну.'),
('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10',
 'Провідний університет Естонії, заснований у 1632 році. Студенти обміну можуть обрати англомовні курси з екології, генетики та молекулярної біології.'),
('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30',
 'Другий за величиною університет Чехії, розташований у Брно. Природничий факультет пропонує англомовні курси для студентів програм обміну.');
"""

# Видаляємо за назвою, а не за повним рядком: після відкату 0003 країна
# приєднується вже через кому, тож формат може відрізнятися від початкового.
DELETE_SQL = "DELETE FROM exchange_exchangeprogram WHERE {};".format(
    " OR ".join("university LIKE '{}%'".format(name) for name in UNIVERSITY_NAMES)
)


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(INSERT_SQL, reverse_sql=DELETE_SQL),
    ]
