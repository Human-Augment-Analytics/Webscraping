import MapComponent from "@/components/MapComponent";
import Nav from "@/components/Nav";

export default function Home() {
  return (
    <main className="flex min-h-screen">
        <Nav />
        <MapComponent />
    </main>
  );
}
