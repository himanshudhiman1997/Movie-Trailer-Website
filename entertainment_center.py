import fresh_tomatoes
import media
"""Information for Tiger Zinda Hai movie."""
tiger = media.Movie("Tiger Zinda Hai",
                    "East Indian agent Tiger joins forces with "\
                    "Pakistani agent Zoya to battle a ruthless "\
                    "militant.",
                    "https://upload.wikimedia.org/wikipedia/en/"\
                    "thumb/5/5e/Tiger_Zinda_Hai_-_Poster.jpg/220"\
                    "px-Tiger_Zinda_Hai_-_Poster.jpg",
                    "https://www.youtube.com/watch?v=ePO5M5DE01I",
                    "Ali Abbas Zafar")
"""Information for Ek Tha Tiger movie."""
ek_tiger = media.Movie("Ek Tha Tiger",
                       "RAW agent Tiger is sent to Dublin to observe "\
                       "an Indian scientist who is suspected of sharing"\
                       " nuclear secrets with the ISI. He meets and falls"\
                       " for his caretaker Zoya, a girl with a dark "\
                       "secret.",
                       "https://i.ytimg.com/vi/uI8Kkj2uBS8/movieposter"\
                       ".jpg",
                       "https://www.youtube.com/watch?v=SmUl0l8qBXw",
                       "Kabir Khan")
"""Information for Raees movie."""
raees = media.Movie("Raees",
                    "Threat looms over bootlegger Raees Alam and his "\
                    "business after ACP Majmudar decides to get the better "\
                    "of him. In order to survive and keep his trade thriving,"\
                    " Raees must overcome these obstacles.",
                    "https://resizing.flixster.com/E0mbSYDhPlpTglw3tbH3Za_D9E"\
                    "k=/206x305/v1.bTsxMjI5NDY4MjtqOzE3NjAyOzEyMDA7Njk0OzkyNQ",
                    "https://www.youtube.com/watch?v=J7_1MU3gDk0",
                    "Rahul Dholakia")
"""Information for Kaabil movie."""
kaabil = media.Movie("Kaabil",
                     "The blissful married lives of Supriya and Rohan,"\
                     " a visually impaired couple, come to a halt when "\
                     "the former is raped by men with political links. "\
                     "When she commits suicide, Rohan vows to take revenge.",
                     "https://timesofindia.indiatimes.com/thumb.cms?"\
                     "msid=56749703&width=218&height=310",
                     "https://www.youtube.com/watch?v=nubDFeiUAsI",
                     "Sanjay Gupta")
"""Information for Border movie."""
border = media.Movie("Border",
                     "A band of 120 soldiers defend their post all night"\
                     " until they receive assistance from the Indian Air"\
                     " Force the next morning.",
                     "https://images-na.ssl-images-amazon.com/images"\
                     "/M/MV5BYzZjNzE4MjMtODExYS00MGJhLWJmZDUtMmJkYWZlN2"\
                     "VjNTkzXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_UX182_CR0,0"\
                     ",182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=aJ-sxaxkoD4",
                     "J. P. Dutta")
"""Information for Shivaay movie."""
shivay = media.Movie("Shivaay",
                      "To unite his daughter Gaura with her Bulgarian mother"\
                      " Olga, Shivaay, an Indian man, travels overseas. On"\
                      " the way, a child trafficker kidnaps Gaura, causing "\
                      "Shivaay to chase him.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/a/a1/"\
                      "Ajay_Devgan%27s_Shivaay_poster.jpg/220px-Ajay_Devgan%"\
                      "27s_Shivaay_poster.jpg",
                      "https://www.youtube.com/watch?v=poLjq0u4_5A",
                      "Ajay Devgan")
"""Information for Dhoom 3 movie."""
dhoom3 = media.Movie("Dhoom 3",
                     "Sahir, a circus entertainer who is trained in magic"\
                     " and acrobatics, turns into a thief to take down a"\
                     " corrupt bank in Chicago in order to avenge his "\
                     "father's death.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/f/f1/"\
                     "Dhoom_3_Film_Poster.jpg/220px-Dhoom_3_Film_Poster.jpg",
                     "https://www.youtube.com/watch?v=yeF_b8EQcK0",
                     "Vijay Krishna Acharya")
"""Information for Student of the Year movie."""
student_of_the_year = media.Movie("Student of the Year",
                                  "Abhimanyu and Rohan are good friends. "\
                                  "However, their friendship is affected "\
                                  "after they compete to win the Student of"\
                                  " The Year title and Abhimanyu falls in"\
                                  " love with Shanaya, Rohan's girlfriend.",
                                  "https://upload.wikimedia.org/wikipedia/en"\
                                  "/thumb/0/00/Student_of_the_Year_Poster.jpg"\
                                  "/220px-Student_of_the_Year_Poster.jpg",
                                  "https://www.youtube.com/watch?v=fivOhPjX"\
                                  "9YM",
                                  "Karan Johar")
"""Array used to store the movies."""
movies = [tiger,ek_tiger,raees,kaabil,border,shivay,dhoom3,student_of_the_year]
fresh_tomatoes.open_movies_page(movies)
