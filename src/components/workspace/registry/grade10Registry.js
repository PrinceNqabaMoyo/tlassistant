import { grade10MathematicsRegistry } from './grade10MathematicsRegistry';
import { grade10MathematicsNewRegistry } from './grade10MathematicsNewRegistry';
import { grade10AccountingRegistry } from './grade10AccountingRegistry';
import { grade10BusinessStudiesRegistry } from './grade10BusinessStudiesRegistry';

export const grade10Registry = {
    ...grade10MathematicsRegistry,
    // Rebuilt maths modes override the legacy ones for migrated topics.
    ...grade10MathematicsNewRegistry,
    ...grade10AccountingRegistry,
    ...grade10BusinessStudiesRegistry,
};
