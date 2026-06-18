import React from 'react';
import { grade7Registry } from './registry/grade7Registry';
import { grade7EmsRegistry } from './registry/grade7EmsRegistry';
import { grade8Registry } from './registry/grade8Registry';
import { grade8EmsRegistry } from './registry/grade8EmsRegistry';
import { grade9Registry } from './registry/grade9Registry';
import { grade9EmsRegistry } from './registry/grade9EmsRegistry';
import { grade10Registry } from './registry/grade10Registry';
import { grade10BusinessStudiesRegistry } from './registry/grade10BusinessStudiesRegistry';
import { grade10BusinessStudiesTerm3Registry } from './registry/grade10BusinessStudiesTerm3Registry';
import { grade11Registry } from './registry/grade11Registry';
import { grade11BusinessStudiesRegistry } from './registry/grade11BusinessStudiesRegistry';
import { grade12Registry } from './registry/grade12Registry';
import WorkspaceModeShell from './shared/WorkspaceModeShell';
import EvaluatedWorkspaceModeShell from './shared/EvaluatedWorkspaceModeShell';

const h = React.createElement;

export const workspaceRegistry = {
    ...grade7Registry,
    ...grade7EmsRegistry,
    ...grade8Registry,
    ...grade8EmsRegistry,
    ...grade9Registry,
    ...grade9EmsRegistry,
    ...grade10Registry,
    ...grade10BusinessStudiesRegistry,
    ...grade10BusinessStudiesTerm3Registry,
    ...grade11Registry,
    ...grade11BusinessStudiesRegistry,
    ...grade12Registry,
};

export const renderFromRegistry = ({ workspaceMode, ctx }) => {
    // Check for marking mode — derive the base and check if scaffold/practice exists
    const markingMatch = workspaceMode?.match(/^(.+)_marking$/);
    if (markingMatch) {
        // Marking route: render shell with marking placeholder (no child content)
        return h(WorkspaceModeShell, {
            workspaceMode,
            setWorkspaceMode: ctx.setWorkspaceMode,
            onBack: ctx.onBack,
            selectedSubject: ctx.selectedSubject,
            selectedGrade: ctx.selectedGrade,
            topic: ctx.topic,
            subscriptionTier: ctx.subscriptionTier,
        });
    }

    const entry = workspaceRegistry[workspaceMode];
    if (!entry) return null;

    const routeResult = entry.render(ctx);
    if (!routeResult) return null;

    if (
        routeResult.type === WorkspaceModeShell
        || routeResult.type === EvaluatedWorkspaceModeShell
        || workspaceMode.includes('accounting')
        || workspaceMode.includes('grade10_bs_')
        || workspaceMode.includes('grade11_bs_')
    ) {
        return routeResult;
    }

    const wrappedChild = React.isValidElement(routeResult)
        ? React.cloneElement(routeResult, { hideConfig: true })
        : routeResult;

    // Wrap the existing scaffold/practice component in the shared shell
    return h(WorkspaceModeShell, {
        workspaceMode,
        setWorkspaceMode: ctx.setWorkspaceMode,
        onBack: ctx.onBack,
        selectedSubject: ctx.selectedSubject,
        selectedGrade: ctx.selectedGrade,
        topic: ctx.topic,
        subscriptionTier: ctx.subscriptionTier,
    }, wrappedChild);
};
