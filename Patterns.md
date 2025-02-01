#Antipatterns

Programmierpatterns sind langweilig. Viel interessanter sind Antipatterns, die entweder bei Verwendung korrekter Patterns im falschen Kontext entstehen oder passieren, wenn der Programmierer an seine fachlichen Grenzen stößt.
Das Resultat ist ähnlich: Am Ende ergeben sich eher suboptimale Konsequenzen.

##Golden Hammer/Law of the Instrument/Maslow's Hammer

Ist ein sehr spannendes Antipattern, das sich an ein Zitat von Abraham Maslow anleht: "Wenn dein einziges Werkzeug ein Hammer ist, sieht jedes Problem wie ein Nagel aus".

Der "Goldene Hammer" ist eine Art "Allzweckwaffe" eines Programmierers, dessen geistige Werkzeugbox zu beschränkt ist, um weitere Methoden zu kennen oder implementieren zu können. Die Hauptlösung, um bestimmte Ziele zu erreichen wird hierbei immer wiederholt, ob passend oder nicht.

Dieses Antipattnern kommt häufig in Systemen und Organisationen vor, die entweder nicht genügend Mittel in die Weiterbilung der Programmierer stecken oder zu sehr auf ein einziges Produkt fokussiert sind.

Es können auch ordentliche Software Patterns zum "Goldenen Hammer" werden. Beispielsweise das Factory-Pattner, das speziell Java-Entwickler am Anfang ihrer Karriere oft lernen und glauben, es in jeglicher passender oder auch unpassender Situation verwenden. Anstelle eines Konstruktors wird das Objekt über eine Methode einer Fabriksklasse erzeugt. Beispielsweise kann es unnötig sein, mehrere Unterklassen zu erstellen - ein gelernter "Fabriksarbeiter" wäre wohl geneigt prophylaktsich für jede neue Klasse in seinem Projekt eine Unterklasse mit Fabriksmethode zu bauen - was die Komplexität des Programms unnötig erhöht und tendenziell auch unintuitiver macht.
Ebenso wird heute der objektorientierte Ansatz oftmals als der einzig Richtige definiert, was dazu führen kann, dass eine prozedurale, kurze, elegante Lösung verworfen wird, um stattdessen eine absurde Anzahl an Objekten zu basteln, die nichts Anderes machen, als sich gegenseitig aufzurufen. https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition hat dies nettwerweise auf die Spitze getrieben.

Ein anderes Beispiel ist die eingangs erwähnte Fokussierung auf ein einziges Produkt. In der Literatur wird gerne eine Datenbank gewählt. Es kann natürlich vorkommen, dass anstatt sich mit der Architektur eines Projekts auseinanderzusetzen lieber auf bestehende Strukturen einer bereits existierenden, zugekauften Lösung zurückgegriffen wird. Die kann dann zu Problemen führen, wenn man seine Produkte modernisieren möchte, in zu vielen Fällen jedoch auf Drittlösungen gesetzt wird, die nicht ersetzbar sind.

##Poltergeist/Gypsy/Gypsy Wagon

Poltergeister sind typischweise sehr kurzlebige, meistens zustandslose Objekte die nichts Anderes machen, als andere Methoden oder Prozesse zu starten, relativ wenig selbst tun, damit meist nur eine Sache implementiert haben und damit meistens nur Ressourcen verbrennen. Das können auch transiente Datenklassen sein.

Es ist nicht immer einfach, Poltergeister von anderen Patterns zu unterscheiden, "Front Controller" zum Beispiel. Oftmals enthalten Poltergeister auch Namenskonventionen wie "manager", "controller", "supervisor", "start_process".

So eine Poltergeist-Klasse kann entweder von einem unerfahrenen Entwickler für objektorientierte Software geschrieben worden sein, oder vorkommen, wenn man eine weitaus komplexere Funktionalität erwartet, die jedoch nicht eingetreten ist.

Diese Klassen sind nicht nur deswegen problematisch, weil sie unnötig Ressourcen verschwenden, sondern auch weil sie es schwerer machen, die Architektur eines Systems zu verstehen und die Abarbeitung des Gesamtprozesses behindern. Oft also eine weitere, unnötige Abstrahierungsschicht einfügen.

Ein einfaches Entfernen der Poltergeister ist nicht einfach so möglich. Die Abhängigkeiten müssen aufgetrennt, refaktoriert und ordentlich neu implementiert werden.
Es kann passieren, dass durch das Entfernen der Poltergeister der Workflow des Programms entfernt wird, was auch dazu führen kann, dass bestehende Klassen neu gruppiert werden müssen.

