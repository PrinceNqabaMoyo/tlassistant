import { grade10MathematicsRegistry } from './grade10MathematicsRegistry';
import { grade10AccountingRegistry } from './grade10AccountingRegistry';
import { grade10BusinessStudiesRegistry } from './grade10BusinessStudiesRegistry';

export const grade10Registry = {
    ...grade10MathematicsRegistry,
    ...grade10AccountingRegistry,
    ...grade10BusinessStudiesRegistry,
};
