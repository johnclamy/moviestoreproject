from django.shortcuts import render


movies = [
    {
        'id': 1, 'name': 'Bitcoin Heist', 'price': 11.99, 'rating': 4,
        'description': """To catch the world's most wanted thief, an Interpol agent assembles a team of elite hackers to plan the ultimate crypto-currency heist."""
    },
    {
        'id': 2, 'name': 'Mountainhead', 'price': 14.99, 'rating': 3,
        'description': """A group of billionaire friends get together against the backdrop of a rolling international crisis."""
    },
    {
        'id': 3, 'name': 'Sinners', 'price': 14.99, 'rating': 4,
        'description': """Trying to leave their troubled lives behind, twin brothers (Michael B. Jordan) return to their hometown to start again, only to discover that an even greater evil is waiting to welcome them back."""
    },
    {
        'id': 4, 'name': 'Fountain of Youth', 'price': 14.99, 'rating': 2,
        'description': """A treasure-hunting mastermind assembles a team for a big adventure. But to outwit and outrun threats at every turn, he'll need someone even smarter, his estranged sister."""
    },
    {
        'id': 5, 'name': 'Mickey 17', 'price': 14.99, 'rating': 3,
        'description': """Mickey 17, known as an "expendable," goes on a dangerous journey to colonize an ice planet."""
    },
    {
        'id': 6, 'name': 'Captain America: Brave New World', 'price': 14.99, 'rating': 2,
        'description': """Anthony Mackie returns as the high-flying hero Sam Wilson, who's officially taken up the mantle of Captain America. After meeting with newly elected U.S. President Thaddeus Ross, Sam finds himself in the middle of an international incident. He must discover the reason behind a nefarious global plot before the true mastermind has the entire world seeing red."""
    },
    {
        'id': 7, 'name': 'Pig', 'price': 11.99, 'rating': 3,
        'description': """A truffle hunter who lives alone in the Oregonian wilderness must return to his past in Portland in search of his beloved foraging pig after she is kidnapped."""
    },
    {
        'id': 8, 'name': 'Black Bag', 'price': 11.99, 'rating': 4,
        'description': """BLACK BAG is a gripping spy drama about legendary intelligence agents George Woodhouse and his beloved wife Kathryn. When she is suspected of betraying the nation, George faces the ultimate test loyalty to his marriage or his country."""
    },
    {
        'id': 9, 'name': 'Mission: Impossible - Dead Reckoning Part One', 'price': 14.99, 'rating': 4,
        'description': """In Mission: Impossible - Dead Reckoning Part One, Ethan Hunt (Tom Cruise) and his IMF team embark on their most dangerous mission yet: To track down a terrifying new weapon that threatens all of humanity before it falls into the wrong hands. With control of the future and the fate of the world at stake, and dark forces from Ethan's past closing in, a deadly race around the globe begins. Confronted by a mysterious, all-powerful enemy, Ethan is forced to consider that nothing can matter more than his mission -- not even the lives of those he cares about most."""
    },
    {
        'id': 10, 'name': 'Warfare', 'price': 14.99, 'rating': 3,
        'description': """Written and directed by, Iraq War, veteran Ray Mendoza and Alex Garland (Civil War, 28 Days Later), Warfare embeds audiences with a platoon of American Navy SEALs on a surveillance mission gone wrong in insurgent territory. A visceral, boots-on-the-ground story of modern warfare and brotherhood, told like never before: in real time and based on the memory of the people who lived it."""
    },
    {
        'id': 11, 'name': 'Companion', 'price': 11.99, 'rating': 3,
        'description': """New Line Cinema--the studio that brought you "The Notebook"--and the unhinged creators of "Barbarian" cordially invite you to experience a new kind of love story..."""
    },
    {
        'id': 12, 'name': 'The Phoenician Scheme', 'price': 11.99, 'rating': 4,
        'description': """The story of a family and a family business."""
    },
]


def index(request):
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies

    return render(
        request,
        'movies/index.html',
        {
            'template_data': template_data
        }
    )
