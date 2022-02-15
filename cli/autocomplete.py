ac_table = {
    'commands': [
        '--help',
        '--version',
        '--version-full',
        'hello',
        'executor',
        'flow',
        'ping',
        'new',
        'gateway',
        'hub',
        'help',
        'pod',
        'deployment',
        'client',
        'export-api',
    ],
    'completions': {
        'hello fashion': [
            '--help',
            '--workdir',
            '--download-proxy',
            '--index-data-url',
            '--index-labels-url',
            '--query-data-url',
            '--query-labels-url',
            '--num-query',
            '--top-k',
        ],
        'hello chatbot': [
            '--help',
            '--workdir',
            '--download-proxy',
            '--index-data-url',
            '--port-expose',
            '--replicas',
            '--unblock-query-flow',
        ],
        'hello multimodal': [
            '--help',
            '--workdir',
            '--download-proxy',
            '--index-data-url',
            '--port-expose',
            '--unblock-query-flow',
        ],
        'hello fork': ['--help', 'fashion', 'chatbot', 'multimodal'],
        'hello': ['--help', 'fashion', 'chatbot', 'multimodal', 'fork'],
        'executor': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--workspace-id',
            '--extra-search-paths',
            '--timeout-ctrl',
            '--k8s-namespace',
            '--k8s-disable-connection-pool',
            '--polling',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--host-in',
            '--native',
            '--entrypoint',
            '--docker-kwargs',
            '--pull-latest',
            '--volumes',
            '--gpus',
            '--host',
            '--port-jinad',
            '--quiet-remote-logs',
            '--upload-files',
            '--disable-remote',
            '--daemon',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--expose-public',
            '--shard-id',
            '--replica-id',
            '--pod-role',
            '--noblock-on-start',
            '--shards',
            '--replicas',
            '--install-requirements',
            '--force-update',
            '--force',
            '--uses-before-address',
            '--uses-after-address',
            '--connection-list',
        ],
        'flow': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--workspace-id',
            '--extra-search-paths',
            '--timeout-ctrl',
            '--k8s-namespace',
            '--k8s-disable-connection-pool',
            '--polling',
            '--uses',
            '--env',
            '--inspect',
        ],
        'ping': ['--help', '--timeout', '--retries'],
        'new': ['--help'],
        'gateway': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--workspace-id',
            '--extra-search-paths',
            '--timeout-ctrl',
            '--k8s-namespace',
            '--k8s-disable-connection-pool',
            '--polling',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--host-in',
            '--native',
            '--prefetch',
            '--title',
            '--description',
            '--cors',
            '--default-swagger-ui',
            '--no-debug-endpoints',
            '--no-crud-endpoints',
            '--expose-endpoints',
            '--uvicorn-kwargs',
            '--compress',
            '--compress-min-bytes',
            '--compress-min-ratio',
            '--protocol',
            '--host',
            '--proxy',
            '--port-expose',
            '--graph-description',
            '--deployments-addresses',
            '--daemon',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--expose-public',
            '--shard-id',
            '--replica-id',
            '--pod-role',
            '--noblock-on-start',
            '--shards',
            '--replicas',
            '--uses-before-address',
            '--uses-after-address',
            '--connection-list',
        ],
        'hub new': [
            '--help',
            '--name',
            '--path',
            '--advance-configuration',
            '--description',
            '--keywords',
            '--url',
            '--add-dockerfile',
        ],
        'hub push': [
            '--help',
            '--no-usage',
            '--verbose',
            '--dockerfile',
            '--tag',
            '--force-update',
            '--force',
            '--secret',
            '--public',
            '--private',
        ],
        'hub pull': [
            '--help',
            '--no-usage',
            '--install-requirements',
            '--force-update',
            '--force',
        ],
        'hub': ['--help', 'new', 'push', 'pull'],
        'help': ['--help'],
        'pod': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--workspace-id',
            '--extra-search-paths',
            '--timeout-ctrl',
            '--k8s-namespace',
            '--k8s-disable-connection-pool',
            '--polling',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--host-in',
            '--native',
            '--entrypoint',
            '--docker-kwargs',
            '--pull-latest',
            '--volumes',
            '--gpus',
            '--host',
            '--port-jinad',
            '--quiet-remote-logs',
            '--upload-files',
            '--disable-remote',
            '--daemon',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--expose-public',
            '--shard-id',
            '--replica-id',
            '--pod-role',
            '--noblock-on-start',
            '--shards',
            '--replicas',
            '--install-requirements',
            '--force-update',
            '--force',
            '--uses-before-address',
            '--uses-after-address',
            '--connection-list',
        ],
        'deployment': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--workspace-id',
            '--extra-search-paths',
            '--timeout-ctrl',
            '--k8s-namespace',
            '--k8s-disable-connection-pool',
            '--polling',
            '--uses',
            '--uses-with',
            '--uses-metas',
            '--uses-requests',
            '--py-modules',
            '--port-in',
            '--host-in',
            '--native',
            '--entrypoint',
            '--docker-kwargs',
            '--pull-latest',
            '--volumes',
            '--gpus',
            '--host',
            '--port-jinad',
            '--quiet-remote-logs',
            '--upload-files',
            '--disable-remote',
            '--daemon',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--expose-public',
            '--shard-id',
            '--replica-id',
            '--pod-role',
            '--noblock-on-start',
            '--shards',
            '--replicas',
            '--install-requirements',
            '--force-update',
            '--force',
            '--uses-before-address',
            '--uses-after-address',
            '--connection-list',
            '--uses-before',
            '--uses-after',
            '--external',
            '--deployment-role',
        ],
        'client': [
            '--help',
            '--host',
            '--proxy',
            '--port',
            '--https',
            '--asyncio',
            '--results-as-docarray',
            '--protocol',
        ],
        'export-api': ['--help', '--yaml-path', '--json-path', '--schema-path'],
    },
}
