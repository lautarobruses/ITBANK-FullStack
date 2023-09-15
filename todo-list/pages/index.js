import Layout from "@/components/layout";
import Inicio from './Inicio';
import Create from './Create';

export default function Home() {
    return (
        <Layout>
            <Inicio />
            <Create />
        </Layout>
    );
}
