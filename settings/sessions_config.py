# 

#     // Rollendefinitionen für Sessions
#     // -------------------------------

    
#     
    
#     Es gibt drei Unterteilungen: Den 
#     Administrator, den erweiterten Nutzer (dieser darf auch in 
#     der Datenbank suchen; z. B. Polizei etc.) und den 
#     normalen Nutzer (dieser darf nur ein Konto erstellen und 
#     Personen, die Obdach gefunden haben, registrieren) 
    
    
#     Wenn Sie selbst eine Instanz der Anwendung bei sich starten
#     wollen, ändern sie im Dictionary *roles* die Werte
#     ('aragorn',...)! Es wäre unsicher, die Werte einfach stehen zu lassen,
#     weil die Anwendung auf Github publiziert wird. 
#     Denken Sie sich einfach andere Werte aus.

#     z. B.:

#         "admin"=>"kanzler",
#         "featured-user"=>"minister",
#         "normal-user"=>"abgeordneter"
    
#     */

roles = {
    "admin": "aragorn",
    "featured-user": "hobbit",
    "normal-user": "orc"
}
    
    
