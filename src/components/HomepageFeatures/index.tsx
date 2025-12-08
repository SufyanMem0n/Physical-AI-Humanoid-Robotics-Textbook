import type {ReactNode} from 'react';
import Link from '@docusaurus/Link';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type ModuleItem = {
  title: string;
  description: ReactNode;
  link: string;
};

const ModuleList: ModuleItem[] = [
  {
    title: 'Part I: Foundations',
    description: (
      <>
        Introduction to Physical AI, ROS 2 essentials, and building your first robotic application.
      </>
    ),
    link: '/docs/Part-I-Foundations/intro',
  },
  {
    title: 'Part II: Digital Twins',
    description: (
      <>
        Master robot modeling with URDF, and create high-fidelity simulations in Gazebo.
      </>
    ),
    link: '/docs/Part-II-Digital-Twins/intro',
  },
  {
    title: 'Part III: NVIDIA Isaac',
    description: (
      <>
        Leverage the power of NVIDIA Isaac Sim for advanced simulation and synthetic data generation.
      </>
    ),
    link: '/docs/Part-III-NVIDIA-Isaac/intro',
  },
  {
    title: 'Part IV: VLA & Humanoids',
    description: (
      <>
        Explore Vision-Language-Action models and the complexities of humanoid robotics.
      </>
    ),
    link: '/docs/Part-IV-VLA-Humanoid/intro',
  },
];

function ModuleCard({title, description, link}: ModuleItem) {
  return (
    <div className="col col--6 margin-bottom--lg">
        <Link to={link} className={styles.moduleCard}>
            <Heading as="h3">{title}</Heading>
            <p>{description}</p>
        </Link>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {ModuleList.map((props, idx) => (
            <ModuleCard key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}