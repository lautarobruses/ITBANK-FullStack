import styles from '@/styles/Login/CheckBox.module.css'

const Checkbox = ({ children }) => {
    return (
        <div className={`${styles.checkBoxContainer}`}>
            <label className={`${styles.label}`}>
                <input className={`${styles.checkBox}`} type="checkbox"/>
                <div className={`${styles.controlIndicator}`}></div>
                {children}
            </label>
        </div>
    )
}

export default Checkbox