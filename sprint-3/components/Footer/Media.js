import styles from '@/styles/Footer/Media.module.css'

import Link from 'next/link'

import FacebookIcon from "@/public/svg/facebook.svg"
import TwitterIcon from "@/public/svg/twitter.svg"
import InstagramIcon from "@/public/svg/instagram.svg"

const Media = () => {
    return (
        <div className={`${styles.media}`}>
            <Link href="https://www.facebook.com" target="_blank" rel="noreferrer" >
                <FacebookIcon />
            </Link>
            <Link href="https://twitter.com" target="_blank" rel="noreferrer">
                <TwitterIcon />
            </Link>
            <Link href="https://www.instagram.com" target="_blank" rel="noreferrer">
                <InstagramIcon />
            </Link>
        </div>
    )
}

export default Media