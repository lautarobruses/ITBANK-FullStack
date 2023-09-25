const generateSiteMap = () => {
    return `
        <?xml version="1.0" encoding="UTF-8"?>
        <urlset 
            xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
            <url>
                <loc>https://www.nexusbank.com/</loc>
                <changefreq>monthly</changefreq>
                <priority>1.0</priority>
            </url>
            <url>
                <loc>https://www.nexusbank.com/cuenta</loc>
                <changefreq>monthly</changefreq>
                <priority>0.8</priority>
            </url>
            <url>
                <loc>https://www.nexusbank.com/cuenta/login</loc>
                <changefreq>monthly</changefreq>
                <priority>1.0</priority>
            </url>
            <url>
                <loc>https://www.nexusbank.com/cuenta/register</loc>
                <changefreq>monthly</changefreq>
                <priority>1.0</priority>
            </url>
            <url>
                <loc>https://www.nexusbank.com/transferencias</loc>
                <changefreq>monthly</changefreq>
                <priority>0.8</priority>
            </url>
            <url>
                <loc>https://www.nexusbank.com/pagos</loc>
                <changefreq>monthly</changefreq>
                <priority>0.8</priority>
            </url>
            <url>
                <loc>https://www.nexusbank.com/prestamos</loc>
                <changefreq>monthly</changefreq>
                <priority>0.8</priority>
            </url>
            <url>
                <loc>https://www.nexusbank.com/coming-soon</loc>
                <changefreq>monthly</changefreq>
                <priority>0.5</priority>
            </url>
        </urlset>
    `
}

export async function getServerSideProps({ res }) {
    const sitemap = generateSiteMap();

    res.setHeader('Content-Type', 'text/xml');
    res.write(sitemap);
    res.end();

    return {
        props: {},
    };
}
   