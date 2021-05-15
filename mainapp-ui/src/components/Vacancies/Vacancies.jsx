import React from "react";
import styles from './Vacancies.module.scss'
import Items from "../Items/Items";

const Vacancies = () => {
    return (
        <div className={styles.wrapper}>
            <div className={styles.vacanciesForYou}>
                <p>Вакансии для Вас</p>
                <div className={styles.items}>
                    <Items/>
                </div>
            </div>

            <div className={styles.vacanciesAll}>
                <p>Все вакансии</p>
                <div className={styles.items}>
                    <Items/>
                </div>
            </div>
        </div>
    )
}
export default Vacancies;