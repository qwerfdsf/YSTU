import React from 'react';
import styles from './Profile.module.scss'
import Skills from './Skills/Skills'
import Information from "./Information/Information";
import Items from '../Items/Items';

const Profile = () => {
    return (
        <div className={styles.wrapper}>

            <div className={styles.info}>
                <p>Общая информация</p>
                <Information/>
            </div>

            <div className={styles.skills}>
                <p>Навыки</p>
                <Skills/>
            </div>

            <div className={styles.events}>
                <p>Завершённые мероприятия</p>
                <Items/>
            </div>

            <div className={styles.projects}>
                <p>Завершённые проекты</p>
                <Items/>
            </div>

        </div>
    )
}

export default Profile;