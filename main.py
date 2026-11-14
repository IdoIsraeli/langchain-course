import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def main():
    print("Hello from langchain-course! please hold")
    info = """Robert Lewandowski (Polish pronunciation: [ˈrɔbɛrt lɛvanˈdɔfskʲi] ⓘ; born 21 August 1988) is a Polish professional footballer who plays as a striker for Major League Soccer club Chicago Fire and captains the Poland national team. Widely regarded as one of the greatest strikers of all time, he is one of only five players to have scored 100 goals with three different clubs,[note 1] ranks third for the all-time top goalscorers in the UEFA Champions League with 109 goals,[4] and ranks joint third for the all-time European men's top goalscorers in international football (92). He has scored over 750 senior career goals for club and country. In addition, he is also one of a select number of players who have amassed over 1,100 career appearances (the first Pole to achieve the feat, since the time matches are recorded).

Beginning his career in the third and second tiers of Polish football with Znicz Pruszków, Lewandowski moved to top-flight Lech Poznań, helping the team win the 2009–10 Ekstraklasa. In 2010, he transferred to Borussia Dortmund, where he won two consecutive Bundesliga titles and the league's top goalscorer award. In 2013, he also featured with Dortmund in the 2013 UEFA Champions League final. Ahead of the 2014–15 season, Lewandowski joined Dortmund's domestic rivals, Bayern Munich, on a free transfer. In Munich, he won the Bundesliga title in all of his eight seasons at the club and was integral in their Champions League win in 2019–20 as part of a treble. Lewandowski was widely expected to win the 2020 Ballon d'Or, but it was not awarded due to the impact of COVID-19. In 2022, he moved to Barcelona, where he won three La Liga titles, the Copa del Rey, and the Pichichi Trophy; his Pichichi Trophy win made him the joint-record holder for most top scorer awards in Europe's top five leagues with eight.[5] Following his departure from Barcelona at the end of the 2025–26 season, Lewandowski joined Major League Soccer club Chicago Fire in June 2026.

A full international for Poland since 2008, Lewandowski has earned 170 caps, and was a member of their team at the UEFA European Championship in 2012, 2016, 2020, and 2024, and the FIFA World Cup in 2018 and 2022. Having captained the national team since 2014, he briefly retired in 2025, before returning and being reinstated as captain later the same year. With 92 international goals, he is the all-time top scorer for Poland.[6] Lewandowski has been named the Polish Footballer of the Year a record thirteen times and the Polish Sports Personality of the Year three times.

Lewandowski won the Best FIFA Men's Player Award in 2020 and 2021. Further awards include the UEFA Men's Player of the Year Award in 2020, the IFFHS World's Best Player in 2020 and 2021, the European Golden Shoe for the 2020–21 and 2021–22 seasons, and the Gerd Müller Trophy in 2021 and 2022. He was runner-up for the Ballon d'Or in 2021. He is one of the most successful players in Bundesliga and Bayern history, being named the VDV Player of the Season (Silver Boot) a record five times and winning the Bundesliga Top Scorer Award in a joint-record seven seasons, among other records."""

    summary_template = """
    Given the information {info} about a person, I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["info"], template=summary_template
    )

    llm = ChatGoogleGenerativeAI(
        model= "gemini-3.5-flash"
    )
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"info": info})
    print(res.text)


if __name__ == "__main__":
    main()
