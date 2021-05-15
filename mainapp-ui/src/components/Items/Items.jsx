import React from "react";
import styles from './Items.module.scss'
import Item from "./Item/Item";

const Items = () => {
    return (
        <div className={styles.wrapper}>
            <div className={styles.item}><Item/></div>
            <div className={styles.item}><Item/></div>
            <div className={styles.item}><Item/></div>
            <div className={styles.item}><Item/></div>
        </div>

    )
}

export default Items;