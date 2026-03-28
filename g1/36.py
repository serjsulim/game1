berichte = [ "Der Umsatz im letzten Quartal war sehr gut. Der Gewinn stieg um 20%. Der Verlust konnte verringert werden. Wir haben unsere Marktstrategie angepasst und konnten neue Kunden gewinnen. Der operative Gewinn hat sich positiv entwickelt und wir erwarten ein weiteres Wachstum im nächsten Quartal.", 
            "Leider mussten wir einen Verlust verzeichnen. Der Markt war schwierig und die Konkurrenz groß. Wir haben Maßnahmen ergriffen, um die Kosten zu senken und unsere Effizienz zu steigern. Trotz des Verlustes sehen wir langfristig positive Perspektiven und arbeiten intensiv an neuen Produkten, um unsere Marktposition zu stärken.",  
            "Der Gewinn ist weiterhin stabil. Wir sehen positive Entwicklungen in allen Bereichen. Besonders in der Region Europa konnten wir unseren Marktanteil ausbauen. Unsere Investitionen in Forschung und Entwicklung zahlen sich aus und wir planen, unsere Produktpalette zu erweitern. Der operative Gewinn zeigt eine solide Entwicklung und wir sind optimistisch für die Zukunft.",  
            "Dieses Jahr war herausfordernd. Der Verlust war hoch, aber wir erwarten eine Verbesserung. Unsere neuen Projekte zeigen vielversprechende Ergebnisse und wir haben wichtige Partnerschaften geschlossen. Die Effizienzprogramme, die wir eingeführt haben, beginnen zu wirken und wir sind zuversichtlich, dass sich der Verlust in den kommenden Quartalen reduzieren wird.",  
            "Dank neuer Strategien konnten wir den Gewinn steigern und Verluste minimieren. Unsere Umsätze in Asien sind stark gestiegen und wir haben neue Märkte erschlossen. Der operative Gewinn ist höher als erwartet und wir haben wichtige Schritte unternommen, um unsere Marktpräsenz weiter auszubauen. Die Zukunftsaussichten sind vielversprechend und wir sind gut positioniert, um weiteres Wachstum zu erzielen.",
            "qwqee qwqwq"
            ]  
kilkist = 0
for i in range(len(berichte)):
    if 'Gewinn' in berichte[i]:
        kilkist += 1
print(f'Слово “Gewinn” міститься у {kilkist} звітах')
dovzina = []
for i in range(len(berichte)):
    dovzina.append(len(berichte[i].split()))
print(f'Найдовший звіт має довжину {max(dovzina)} слів, а найкоротший {min(dovzina)} слів')
