import React from "react";
import styles from './Portfolio.module.scss'
import Items from '../Items/Items';

const Portfolio = () => {
    return (
        <div className={styles.wrapper}>
            <div className={styles.events}>
                <p>Завершённые мероприятия</p>
                <div className={styles.main}>
                    <div className={styles.items}>
                    </div>
                    <div className={styles.edit}>
                        <p>
                            Вы не учавствовали в мероприятиях
                        </p>
                        <p>
                            Добавить результаты
                            <button className={styles.add}>+</button>
                        </p>
                    </div>
                </div>
            </div>
            <div className={styles.projects}>
                <p>Личные проекты</p>
                <div className={styles.main}>
                    <div className={styles.items}>
                    </div>
                    <div className={styles.edit}>
                        <p>
                            У вас нет личных проектов
                        </p>
                        <p>
                            Добавить проект
                            <button className={styles.add}>+</button>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Portfolio;