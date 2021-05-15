import React from 'react';
import styles from './MainHeader.module.scss'
import {NavLink} from 'react-router-dom';
import logo from '../icon/logo.svg'
import user from '../icon/user.svg'
import settings from '../icon/settings.svg'
import notification from '../icon/notification.svg'
import exit from '../icon/exit.svg'

const MainHeader = () => {
    return (
        <div className={styles.wrapper}>
            <img className={styles.logo} src={logo} alt="YSTU"/>
            <div className={styles.profile}>
                <NavLink to="/user" target="_blank"><img className={styles.user} src={user} alt=""/></NavLink>
                <span className={styles.profileName}>Перфильев В.С.</span>
                <NavLink to="/setting"><img className={styles.settings} src={settings} alt=""/></NavLink>
                <NavLink to="/notification"><img className={styles.notification} src={notification} alt=""/></NavLink>
                <NavLink to="/exit"><img className={styles.exit} src={exit} alt=""/></NavLink>
            </div>
        </div>
    )
}

export default MainHeader;