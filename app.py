import streamlit as st

# Configurer la page
st.set_page_config(page_title="Les Cinémas de la Creuse", layout="wide")

# Créer un en-tête avec le logo et le titre
header_col1, header_col2 = st.columns([1, 4])
with header_col1:
    st.image(
        "https://static.vecteezy.com/system/resources/previews/000/454/244/original/vector-cinema-icons-concept.jpg", 
        width=200, 
        caption="Logo"
    )
with header_col2:
    st.title("🎥 Les Cinémas de la Creuse")
    st.subheader("Trouvez votre film")

# Créer une barre de navigation avec des onglets
tabs = ["Accueil", "Fiction", "Animation", "Documentaire", "Comédie"]
selected_tab = st.radio(
    "Navigation",
    tabs,
    horizontal=True
)

st.markdown("---")  # Séparer visuellement la navigation du contenu

# Données des films avec affiches et descriptions
movies = [
    {
        "title": "Transformers",
        "category": "Animation",
        "year": 2023,
        "actors": ["Chris Hemsworth", "Scarlett Johansson"],
        "description": "Un préquel animé explorant les origines des Transformers.",
        "image": "https://www.premiere.fr/sites/default/files/styles/scale_crop_336x486/public/2018-04/Transformers.jpg",
        "trailer": "https://www.youtube.com/watch?v=exemple",
        "rating": 8.7,
    },
    {
        "title": "Haikyuu!! La Guerre des Poubelles",
        "category": "Animation",
        "year": 2023,
        "actors": ["Ayumu Murase", "Kaito Ishikawa"],
        "description": "Une bataille épique et hilarante sur le terrain de volley.",
        "image": "https://th.bing.com/th/id/OIP.NiU16SZkEcQkcXvXWJnUKgHaLH?rs=1&pid=ImgDetMain",
        "trailer": "https://www.youtube.com/watch?v=exemple",
        "rating": 9.0,
    },
    {
        "title": "Spider-Man: Across the Spider-Verse",
        "category": "Animation",
        "year": 2023,
        "actors": ["Shameik Moore", "Hailee Steinfeld"],
        "description": "Une aventure multidimensionnelle avec Spider-Man.",
        "image": "https://www.dolby.com/siteassets/xf-site/content-detail-pages/sv2_1280x1920_stothard_dolby_02.jpg",
        "trailer": "https://www.youtube.com/watch?v=exemple",
        "rating": 9.2,
    },
    {
        "title": "Dune: Deuxième partie",
        "category": "Fiction",
        "year": 2024,
        "actors": ["Timothée Chalamet", "Zendaya", "Oscar Isaac"],
        "description": "Suite épique de l'adaptation de Frank Herbert.",
        "image": "https://fr.web.img6.acsta.net/pictures/23/05/03/11/51/2350536.jpg",
        "trailer": "https://www.youtube.com/watch?v=exemple",
        "rating": 9.1,
    },
    {
        "title": "Rebel Moon: Partie 1 - Calice de sang",
        "category": "Fiction",
        "year": 2023,
        "actors": ["Charlie Hunnam", "Sofia Boutella", "Michiel Huisman"],
        "description": "Une bataille pour la survie d'une colonie lointaine.",
        "image": "https://image.tmdb.org/t/p/w500/uiYV2ldUZPDDhgJ6SdXKKB4HRhS.jpg",
        "trailer": "https://www.youtube.com/watch?v=exemple",
        "rating": 8.5,
    },
    # Ajout d'autres films ici...
]

# Générer la liste des acteurs uniques et triés
all_actors = sorted(set(actor for movie in movies for actor in movie["actors"]))

# Filtres dans la barre latérale
st.sidebar.header("Filtres supplémentaires")
selected_year = st.sidebar.selectbox("Filtrer par année :", ["Toutes"] + list(range(1960, 2025)))
selected_actor = st.sidebar.selectbox("Filtrer par acteur :", ["Tous"] + all_actors)

# Fonction de filtrage des films
def filter_movies(movies, category, year, actor):
    filtered = movies.copy()
    
    # Filtrer par catégorie si ce n'est pas "Accueil" (qui affiche tous les films)
    if category != "Accueil":
        filtered = [movie for movie in filtered if movie["category"] == category]
    
    # Filtrer par année
    if year != "Toutes":
        filtered = [movie for movie in filtered if movie["year"] == year]
    
    # Filtrer par acteur
    if actor != "Tous":
        filtered = [movie for movie in filtered if actor in movie["actors"]]
    
    return filtered

# Appliquer les filtres
filtered_movies = filter_movies(movies, selected_tab, selected_year, selected_actor)

# Affichage des films filtrés
if selected_tab == "Accueil":
    st.write("## Bienvenue sur Les Cinémas de la Creuse 🎬")
    st.write("Découvrez nos films disponibles par catégorie et trouvez votre prochain film à regarder !")

st.write("### Films disponibles :")
if not filtered_movies:
    st.write("### Aucun film ne correspond aux critères de filtrage.")
else:
    for movie in filtered_movies:
        st.image(movie["image"], caption=movie["title"], use_column_width=True)
        st.write(f"**{movie['title']}** ({movie['year']})")
        st.write(f"*Catégorie* : {movie['category']}")
        st.write(f"*Description* : {movie['description']}")
        st.write(f"⭐ **Note** : {movie['rating']}")
        st.markdown(f"[🎬 Voir la bande-annonce]({movie['trailer']})")
        st.markdown("---")
