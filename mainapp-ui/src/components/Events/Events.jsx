import React from "react";
import styles from './Events.module.scss'
import Items from "../Items/Items";

const Events = () => {
    return (
        <div className={styles.wrapper}>
            <div className={styles.eventsForYou}>
                <p>Мероприятия для Вас</p>
                <div className={styles.items}>
                    <Items/>
                </div>
            </div>
            <div className={styles.eventsAll}>
                <p>Все мероприятия</p>
                <div className={styles.items}>
                    <Items/>
                </div>

                <div className={styles.eventsCompleted}>
                    <p>Завершённые мероприятия</p>
                    <div className={styles.items}>
                        <Items/>
                    </div>
                </div>
            </div>
        </div>
    )
}
export default Events;
