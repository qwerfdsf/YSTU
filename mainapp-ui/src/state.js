import information from './components/Header/icon/information.svg'
import skills from './components/Header/icon/skills.svg'
import portfolio from './components/Header/icon/portfolio.svg'
import events from './components/Header/icon/events.svg'
import vacancies from './components/Header/icon/vacancies.svg'
import leaderboard from './components/Header/icon/leaderboard.svg'

let state;
state = {
    header: {
        navbarItem: [
            {src: information, item: 'Информация', link: '/profile'},
            // {src: skills, Item: 'Навыки', link: '/skills'},
            {src: portfolio, item: 'Портфолио', link: '/portfolio'},
            {src: events, item: 'Мероприятия', link: '/events'},
            {src: vacancies, item: 'Вакансии', link: '/vacancies'},
            {src: leaderboard, item: 'Рейтинг', link: '/rating'}
        ]
    }
};

export default state;

