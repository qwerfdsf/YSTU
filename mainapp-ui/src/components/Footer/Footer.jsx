import React from 'react';
import styles from './Footer.module.scss'
import vk from './icons/vk.svg'
import inst from './icons/inst.svg'

const Footer = () => {
    return (
        <div className={styles.footer}>
            <div className={styles.wrapper}>
                <div className={styles.social}>
                    <a href="https://vk.com/ystu" target='_blank'><img src={vk} alt="VK"/></a>
                    <a href="https://www.instagram.com/ystu.ru/" target='_blank'><img src={inst} alt="INS"/></a>
                </div>
                <div className={styles.copyright}>
                    <span>© 2021, ФГБОУ ВО «ЯГТУ»</span>
                </div>
                <div className={styles.techSupport}>
                    <a href="">Тех. Поддержка</a>
                </div>
            </div>
        </div>
    )
}

export default Footer;